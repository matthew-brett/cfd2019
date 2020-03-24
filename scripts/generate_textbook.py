from subprocess import check_call
import os
import os.path as op
import shutil as sh
from collections import namedtuple
from contextlib import contextmanager
import yaml
from glob import glob
from uuid import uuid4
import re
import argparse

from nbclean import NotebookCleaner
import nbformat as nbf
import nbconvert as nbc
from tqdm import tqdm
import numpy as np

from jinja2 import Template

from traitlets.config import Config
from nbconvert.writers import FilesWriter
from nbconvert.preprocessors import ExecutePreprocessor

CONTENT_EXTS = ('.ipynb', '.md', '.Rmd')


# Store document information from SUMMARY.md file line.
SummaryEntry = namedtuple('SummaryEntry', 'title link level in_bar')


def _markdown_to_files(path_markdown, indent=2):
    """Takes a markdown file containing chapters/sub-headings and
    converts it to a file structure we can use to build a side bar."""

    with open(path_markdown, 'r') as ff:
        lines = ff.readlines()

    files = []
    for line in lines:
        sline = line.strip()
        if not sline.startswith('* '):
            continue
        in_bar = not sline.startswith('* -')
        title = _between_symbols(line, '[', ']')
        link = _between_symbols(line, '(', ')')
        spaces = len(line) - len(line.lstrip(' '))
        level = int(spaces / indent)
        files.append(SummaryEntry(title, link, level, in_bar))
    return files


def _strip_suffixes(string, suffixes=None):
    """Remove suffixes so we can create links."""
    suffixes = ['.ipynb', '.md'] if suffixes is None else suffixes
    for suff in suffixes:
        string = string.replace(suff, '')
    return string


def _between_symbols(string, c1, c2):
    """Grab characters between symbols in a string.
    Will return empty string if nothing is between c1 and c2."""
    for char in [c1, c2]:
        if char not in string:
            raise ValueError("Couldn't find character {} in string {}".format(
                char, string))
    return string[string.index(c1)+1:string.index(c2)]


def _case_sensitive_fs(path):
    """ True when filesystem at `path` is case sensitive, False otherwise
    """
    root = op.join(path, uuid4().hex)
    fnames = [root + suffix for suffix in 'aA']
    try:
        for fname in fnames:
            with open(fname, 'wt') as fobj:
                fobj.write('text')
        written = glob(root + '*')
    finally:
        for fname in written:
            os.unlink(fname)
    return len(written) == 2


def _split_yaml(lines):
    yaml0 = None
    for i, L in enumerate(lines):
        L = L.strip()
        if yaml0 is None:
            if L == '---':
                yaml0 = i
            elif L:
                break
        elif L == '---':
            return lines[yaml0 + 1:i], lines[i + 1:]
    return [], lines


def test__split_yaml():
    # Run with
    # pytest scripts/generate_notebook.py
    assert _split_yaml([]) == ([], [])
    assert _split_yaml(['foo\n', 'bar\n']) == ([], ['foo\n', 'bar\n'])
    assert _split_yaml(['---\n', 'foo\n', 'bar\n']) == ([], ['---\n', 'foo\n', 'bar\n'])
    exp = ['---\n', 'foo\n', '---\n']
    assert _split_yaml(exp) == (['foo\n'], [])
    assert (_split_yaml(['---\n', 'foo\n', '---\n', 'baz\n', 'barf\n']) ==
            (['foo\n'], ['baz\n', 'barf\n']))
    assert (_split_yaml(['---\n', 'foo\n', 'bar\n', '---\n', 'baz\n', 'barf\n']) ==
            (['foo\n', 'bar\n'], ['baz\n', 'barf\n']))
    assert (_split_yaml(['\n', '\n', '---\n', 'foo\n', '---\n', 'baz\n', 'barf\n']) ==
            (['foo\n'], ['baz\n', 'barf\n']))
    assert (_split_yaml(['   \n', ' \n', '---\n', 'foo\n', '---\n', 'baz\n', 'barf\n']) ==
            (['foo\n'], ['baz\n', 'barf\n']))


def mkdir_if_missing(path):
    if not op.isdir(path):
        os.makedirs(path)


class CodeExecutePreprocessor(ExecutePreprocessor):
    """ ExecutePreprocessor that runs initial code in notebook.
    """

    pre_code = None

    @contextmanager
    def setup_preprocessor(self, nb, resources, km=None, **kwargs):
        cm = super().setup_preprocessor(nb, resources, km=None, **kwargs)
        with cm as args:
            if self.pre_code:
                self.kc.execute(self.pre_code, silent=True)
            yield args


def execute_nb(nb, cwd=None, km=None, default_pre=None, **kwargs):
    """ Execute code in notebook `nb`, running pre code as necessary

    Will execute code in `default_pre` string before executing notebook, unless
    the notebook has a `jupyterbook` field in the `metadata`, containing the
    `pre_code` field, in which case we use the contents of this field instead.

    Parameters
    ----------
    nb : NotebookNode
        The notebook object to be executed.
    cwd : None or str, optional
        If supplied, the kernel will run in this directory.
    km : None or KernelManager, optional
        If supplied, the specified kernel manager will be used for code
        execution.
    default_pre : None or str, optional
        String containing default code to execute before notebook code.  This
        code overridden by presence of notebook metadata field `jupyterbook:
        pre_code`.
    kwargs :
      Any other options for ExecutePreprocessor, e.g. timeout, kernel_name

    Returns
    -------
    ex_nb : NotebookNode
      The notebook object after execution.
    """
    ep = CodeExecutePreprocessor(**kwargs)
    ep.pre_code = nb['metadata'].get(
        'jupyterbook', {}).get(
            'pre_code', default_pre)
    resources = {}
    if cwd is not None:
        resources['metadata'] = {'path': cwd}
    return ep.preprocess(nb, resources, km=km)[0]


class SiteBuilder:

    def __init__(self, site_root, execute=False, overwrite=False):
        site_root = op.abspath(site_root)
        self.site_root = site_root
        self.execute = execute
        self.overwrite = overwrite
        self.site_textbook = op.join(site_root, '_data', 'textbook.yml')
        self.config_file = op.join(site_root, '_config.yml')
        self.template_path = op.join(site_root, 'assets', 'templates', 'jekyllmd.tpl')
        self.textbook_folder_name = '_chapters'
        self.notebooks_folder_name = 'notebooks'
        self.textbook_folder = op.join(site_root, self.textbook_folder_name)
        self.notebooks_folder = op.join(site_root, self.notebooks_folder_name)
        self.images_folder = op.join(site_root, 'images')
        self.markdown_file = op.join(site_root, 'SUMMARY.md')

        mkdir_if_missing(self.textbook_folder)

        self.cased_fs = _case_sensitive_fs(self.textbook_folder)

        # Load the yaml for this site
        with open(self.config_file, 'r') as ff:
            self.site_yaml = yaml.load(ff.read())
        # Load the textbook ymal for this site
        if not op.exists(self.site_textbook):
            with open(self.site_textbook, 'w') as ff:
                pass
        with open(self.site_textbook, 'r') as ff:
            textbook_yaml = yaml.load(ff.read())
        textbook_yaml = {} if textbook_yaml is None else textbook_yaml
        self.textbook_yaml = textbook_yaml
        # Output directory for processed notebooks.
        # None means leave in input notebook folder.
        self.nb_folder = None
        self.nb_folder_name = self.site_yaml.get('nb_folder_name')
        if self.nb_folder_name:
            self.nb_folder = op.join(site_root, self.nb_folder_name)
            mkdir_if_missing(self.nb_folder)
        self.site_dict = self._get_site_dict()
        self.default_pre = self.site_yaml.get('pre_code')

    def _get_site_dict(self):
        site = {}
        sy = self.site_yaml
        site['baseurl'] = sy['url'] + sy['baseurl']
        return site

    def _prepare_link(self, link):
        """Prep the formatting for a link."""
        link = _strip_suffixes(link)
        link = link.lstrip('._')
        link = link.replace(self.notebooks_folder_name + os.sep,
                            self.textbook_folder_name.lstrip('_') + os.sep)
        return link

    def _clean_lines(self, lines, filepath):
        """Replace images with jekyll image root and add escape chars as needed."""
        inline_replace_chars = ['#']
        for ii, line in enumerate(lines):
            # Images: replace absolute nbconvert image paths to baseurl paths
            path_rel_root = op.relpath(self.site_root, op.dirname(filepath))
            line = line.replace(self.images_folder,
                                op.join(path_rel_root, 'images'))

            # Adding escape slashes since Jekyll removes them
            # Make sure we have at least two dollar signs and they
            # Aren't right next to each other
            dollars = np.where(['$' == char for char in line])[0]
            if len(dollars) > 2 and all(ii > 1 for ii in (dollars[1:] - dollars[:1])):
                for char in inline_replace_chars:
                    line = line.replace('\\{}'.format(char), '\\\\{}'.format(char))
            line = line.replace(' \\$', ' \\\\$')
            # Escaped dollar could be at beginning of line
            if line.startswith('\\$'):
                line = '\\' + line
            lines[ii] = line
        return lines

    def _generate_sidebar(self, files):
        """Generate sidebar text for the textbook, add it to the textbook yaml
        """
        sidebar_text = []
        sidebar_text.append({'title': 'Home', 'class': 'level_0', 'url': '/'})
        chapter_ix = 1
        for ix_file, se in list(enumerate(files)):
            title = se.title
            if not se.in_bar:
                continue
            if se.level > 0 and len(se.link) == 0:
                continue
            if se.level == 0:
                if self.site_yaml.get('number_chapters', False) is True:
                    title = '{}. {}'.format(chapter_ix, title)
                chapter_ix += 1
            new_link = self._prepare_link(se.link)
            new_item = {'title': title, "class":
                        "level_{}".format(se.level),
                        'url': new_link}
            if se.level == 0:
                if ix_file != (len(files) - 1) and files[ix_file + 1].level:
                    new_item['children'] = []
                sidebar_text.append(new_item)
            else:
                sidebar_text[-1]['children'].append(new_item)

            # Keep track of the URL for the first file in the textbook
            if ix_file == 0:
                self.textbook_yaml['first_chapter_url'] = new_link

        self.textbook_yaml['chapters'] = sidebar_text

    def _copy_non_content_files(self):
        """Copy non-markdown/notebook files in the notebooks/ folder into Chapters so relative links work."""
        all_files = glob(op.join(self.notebooks_folder, '**', '*'),
                         recursive=True)
        non_content_files = [ii for ii in all_files
                            if not any(ii.endswith(ext) for ext in CONTENT_EXTS)]
        for ifile in non_content_files:
            if op.isdir(ifile):
                continue
            # Convert the old link to the new path, note this may change folder name structure
            old_link = ifile.split(self.notebooks_folder)[-1]
            new_link = self._prepare_link(old_link)

            # The folder name may change if the permalink sanitizing changes it.
            # this ensures that a new folder exists if needed
            new_path = ifile.replace(
                self.notebooks_folder, self.textbook_folder).replace(
                    old_link, new_link)
            if not op.isdir(op.dirname(new_path)):
                os.makedirs(op.dirname(new_path))
            sh.copy2(ifile, new_path)

    def _fill_markdown(self, source):
        # Remove any tags.
        source = re.sub("{% .*? %}", "", source)
        template = Template(source)
        return template.render(site=self.site_dict)

    def _proc_out_nb(self, nb_fname):
        with open(nb_fname, 'rt') as fobj:
            nb = nbf.read(fobj, 4)
        for cell in nb.cells:
            if cell['cell_type'] == 'code':
                # Clear output.
                cell['execution_count'] = None
                cell['outputs'] = []
            elif cell['cell_type'] == 'markdown':
                # Process markup.
                cell['source'] = self._fill_markdown(cell['source'])
        with open(nb_fname, 'wt') as fobj:
            nbf.write(nb, fobj)

    def _copy_clean_notebook(self, link):
        out_dir = op.dirname(link).replace(
            self.notebooks_folder_name, self.nb_folder_name)
        out_path = op.join(out_dir, op.basename(link))
        mkdir_if_missing(out_dir)
        sh.copy2(link, out_dir)
        self._proc_out_nb(out_path)
        return op.sep.join([out_dir, op.basename(link)])

    def _nb2md(self, nb, out_folder, out_base):
        """Run nbconvert on notebook, output to the output folder
        """
        c = Config()
        c.Application.log_level = 'CRITICAL'
        md_exporter = nbc.MarkdownExporter(config=c)
        md_exporter.template_file = self.template_path
        # Image output path - remove _ so Jekyll will copy them over
        out_files_dir = op.join(self.images_folder, out_folder.lstrip('_'))
        # Set base name via unique_key as seed for resources dict.
        body, resources = md_exporter.from_notebook_node(
            nb, resources= {'unique_key': out_base,
                            'output_files_dir': out_files_dir})
        c.FilesWriter.build_directory = out_folder
        FilesWriter(config=c).write(body, resources, notebook_name=out_base)

    def _process_notebook(self, link, new_folder):
        nb = nbf.read(link, nbf.NO_CONVERT)
        site_yaml = self.site_yaml
        if self.execute:
            nb = execute_nb(nb,
                            cwd=op.dirname(link),
                            default_pre=self.default_pre)
        # Clean up the file before converting
        cleaner = NotebookCleaner(nb)
        cleaner.remove_cells(empty=True)
        if site_yaml.get('hide_cell_text', False):
            cleaner.remove_cells(search_text=site_yaml.get('hide_cell_text'))
        if site_yaml.get('hide_code_text', False):
            cleaner.clear(kind="content",
                          search_text=site_yaml.get('hide_code_text'))
        nb = cleaner.ntbk
        # Beware! By default, this cleans warnings etc from the output.
        # Set metadata in notebook YaML to allow stderr.
        if not nb['metadata'].get('jupyterbook', {}).get('show_stderr', False):
            cleaner.clear('stderr')
        self._process_nb_for_md(nb)
        # Convert notebook to markdown
        out_base, _ = op.splitext(op.basename(link))
        self._nb2md(nb, new_folder, out_base)

    def _process_nb_for_md(self, nb):
        """ Process markdown from (possibly executed) notebook `nb`
        """
        self._clean_md_headers(nb)
        self._strip_tracebacks(nb)

    def _clean_md_headers(self, nb):
        """Clean up cell text of an nbformat NotebookNode."""
        # Remove '#' from the end of markdown headers
        for cell in nb.cells:
            if cell.cell_type == "markdown":
                cell_lines = cell.source.split('\n')
                for ii, line in enumerate(cell_lines):
                    if line.startswith('#'):
                        cell_lines[ii] = line.rstrip('#').rstrip()
                cell.source = '\n'.join(cell_lines)

    def _strip_tracebacks(self, nb):
        # Strip error traceback to first, last line
        for cell in nb.cells:
            if cell['cell_type'] != 'code' or 'outputs' not in cell:
                continue
            for output in cell['outputs']:
                if (output['output_type'] != 'error' or
                    'traceback' not in output):
                    continue
                tb = output['traceback']
                if len(tb) == 1:
                    # Syntax errors don't have multiline tracebacks.
                    assert ('SyntaxError' in tb[0] or
                            'IndentationError' in tb[0])
                    continue
                tb[:] = ['\n'.join([tb[1], '   ...', tb[-1]])]

    def _write_out_md(self,
                      link,
                      new_file_path,
                      files,
                      ix_file,
                      title,
                      nb_link=None,
                     ):
        nb_link = link.lstrip('./') if nb_link is None else nb_link
        # Collect previous/next md file for pagination
        if ix_file == 0:
            prev_page_link = ''
            prev_file_title = ''
        else:
            prev_file_title, prev_page_link, _, _ = files[ix_file-1]
            prev_page_link = self._prepare_link(prev_page_link)

        if ix_file == len(files) - 1:
            next_page_link = ''
            next_file_title = ''
        else:
            next_file_title, next_page_link, _, _ = files[ix_file+1]
            next_page_link = self._prepare_link(next_page_link)

        # Extra slash to the inline math before `#` since Jekyll strips it
        with open(new_file_path, 'r') as ff:
            lines = ff.readlines()
        lines = self._clean_lines(lines, new_file_path)

        # Split off original yaml
        yaml_orig, lines = _split_yaml(lines)

        # Front-matter YAML
        yaml_fm = ['---']

        if link.endswith('.ipynb'):
            yaml_fm += ['interact_link: {}'.format(nb_link)]
        yaml_fm += ["title: '{}'".format(title)]
        page_link = self._prepare_link(link)
        yaml_fm += ["permalink: '{}'".format(page_link)]
        yaml_fm += ['previouschapter:']
        yaml_fm += ['  url: {}'.format(self._prepare_link(prev_page_link).replace('"', "'"))]
        yaml_fm += ["  title: '{}'".format(prev_file_title)]
        yaml_fm += ['nextchapter:']
        yaml_fm += ['  url: {}'.format(self._prepare_link(next_page_link).replace('"', "'"))]
        yaml_fm += ["  title: '{}'".format(next_file_title)]
        # In case pre-existing links are sanitized
        sanitized = page_link.lower().replace('_', '-')
        if not self.cased_fs and page_link.lower() == sanitized:
            raise RuntimeError('Redirect {} clashes with page {} '
                            'on case-insensitive FS'.format(
                                sanitized, page_link))
        yaml_fm += ["redirect_from:"]
        yaml_fm += ["  - '{}'".format(sanitized)]
        if ix_file == 0 and self.site_yaml.get('textbook_only') is True:
            yaml_fm += ["  - '/'"]
        yaml_fm = [ii + '\n' for ii in yaml_fm]
        # Add back any original YaML, and end marker
        yaml_fm += yaml_orig + ['---\n']
        lines = yaml_fm + lines

        # Write the result
        with open(new_file_path, 'w') as ff:
            ff.writelines(lines)

    def build(self):
        # --- Collect the files we'll convert over ---
        files = _markdown_to_files(self.markdown_file)

        # --- Loop through all ipynb/md files, convert to md as necessary and copy. ---
        n_skipped_files = 0
        n_built_files = 0
        for ix_file, (title, link, level, _) in tqdm(list(enumerate(files))):
            if len(link) == 0:
                continue
            if not op.exists(link):
                raise ValueError("Could not find file {}.".format(link))

            # Check new folder / file path
            filename = op.basename(link)
            new_folder = op.dirname(link).replace(
                self.notebooks_folder_name, self.textbook_folder_name)
            out_md_file_path = op.join(new_folder,
                                    filename.replace('.ipynb', '.md'))

            if self.overwrite is False and op.exists(out_md_file_path):
                n_skipped_files += 1
                continue

            mkdir_if_missing(new_folder)

            # Convert notebooks or just copy md if no notebook.
            nb_link = None
            if link.endswith('.ipynb'):
                if self.nb_folder:
                    nb_link = self._copy_clean_notebook(link)
                self._process_notebook(link, new_folder)
            elif link.endswith('.md'):
                # If a non-notebook file, just copy it over.
                # If markdown we'll add frontmatter later
                sh.copy2(link, out_md_file_path)
            else:
                raise ValueError("Files must end in ipynb or md")
            self._write_out_md(link,
                               out_md_file_path,
                               files,
                               ix_file,
                               title,
                               nb_link)
            n_built_files += 1

        print("\n***\nGenerated {} new files\nSkipped {} already-built files"
              .format(n_built_files, n_skipped_files))
        if n_built_files == 0:
            print("\nDelete the markdown files in '{}' for any pages "
                  "that you wish to re-build.".format(
                      self.textbook_folder_name))
        print('***\n')
        # Generate sidebar, replacing the old one if it exists
        self._generate_sidebar(files)

        # Copy non-markdown files in notebooks/ in case they're referenced in the notebooks
        print('Copying non-content files inside `notebooks/`...')
        self._copy_non_content_files()

        # Update textbook yaml
        print('Generating sidebar data...')
        with open(self.site_textbook, 'w') as ff:
            yaml.dump(self.textbook_yaml, ff, default_flow_style=False)
        with open(self.site_textbook, 'r') as ff:
            lines = '### PROGRAMATICALLY GENERATED, DO NOT MODIFY\n' + ff.read()
        with open(self.site_textbook, 'w') as ff:
            ff.write(lines)
        print('Done!')


def main():
    description = ("Convert a collection of Jupyter Notebooks into Jekyll "
                   "markdown suitable for a course textbook.")
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--site_root",
                        default=op.join(op.dirname(op.abspath(__file__)), '..'),
                        help="Path to the root of the textbook repository.")
    parser.add_argument("--overwrite", action='store_true',
                        default=False,
                        help="Overwrite md files if they already exist.")
    parser.add_argument("--execute", action='store_true',
                        default=False,
                        help="Execute notebooks before converting to MD.")
    args = parser.parse_args()
    builder = SiteBuilder(args.site_root, args.execute, args.overwrite)
    builder.build()


if __name__ == '__main__':
    main()
