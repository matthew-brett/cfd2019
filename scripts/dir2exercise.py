#!/usr/bin/env python
""" Build zip file OKpy exercise from directory
"""

import os
import os.path as op
import sys
from argparse import ArgumentParser
import re

import yaml
from jinja2 import Template

from rmdex.exerciser import (make_exercise, make_solution, write_utf8,
                             read_utf8)


HERE = op.dirname(op.realpath(__file__))
SITE_ROOT = op.realpath(op.join(HERE, '..'))
sys.path.append(HERE)

import build_exercise as b_e
import grade_oknb as gok


TEMPLATE_RE = re.compile('_template\.Rmd$')


def get_site_dict(site_config):
    with open(site_config, 'r') as ff:
        site = yaml.load(ff.read())
    # Get full baseurl from _config.yml format.
    if not site['baseurl'].startswith('http') and 'url' in site:
        baseurl = site['url'] + site['baseurl']
        site = dict(baseurl=baseurl)
    return site


def render_template(text, site_config):
    site_dict = get_site_dict(site_config)
    template = Template(text)
    return template.render(site=site_dict)


def process_dir(path, out_path, grade=False, site_config=None):
    templates = [fn for fn in os.listdir(path) if TEMPLATE_RE.search(fn)]
    if len(templates) == 0:
        raise RuntimeError('No _template.Rmd in directory')
    if len(templates) > 1:
        raise RuntimeError('More than one _template.Rmd in directory')
    template_fname = op.join(path, templates[0])
    template = read_utf8(template_fname)
    if site_config:
        template = render_template(template, site_config)
    exercise_fname = TEMPLATE_RE.sub('.Rmd', template_fname)
    write_utf8(exercise_fname, make_exercise(template))
    solution_fname = TEMPLATE_RE.sub('_solution.Rmd', template_fname)
    write_utf8(solution_fname, make_solution(template))
    b_e.process_nb(exercise_fname, execute=False)
    if grade:
        grades = gok.grade_nb_fname(solution_fname, path)
        gok.print_grades(grades)
        if not all(grades.values()):
            raise RuntimeError('One or more grades 0')
    b_e.pack_exercise(exercise_fname, out_path)


def find_site_config(dir_path, filenames=('course.yml', '_config.yml')):
    """ Iterate to parents to locate one of filenames specified in `filenames`.
    """
    dir_path = op.realpath(dir_path)
    while True:
        for fn in filenames:
            pth = op.join(dir_path, fn)
            if op.isfile(pth):
                return pth
        prev_dir_path = dir_path
        dir_path = op.realpath(op.join(dir_path, '..'))
        if (dir_path == prev_dir_path or  # We hit root.
            not prev_dir_path.startswith(dir_path)): # We hit fs boundary.
            break
    return None


def main():
    parser = ArgumentParser()
    parser.add_argument('dir', help="Directory of exercise")
    parser.add_argument('--no-grade', action='store_true',
                        help='If specified, do not grade solution notebook')
    parser.add_argument('--out-path',
                        help='Output path for zipped exercise'
                        '(default is ../../exercises)'
                       )
    parser.add_argument('--site-config',
                        help='Path to configuration file for course '
                        '(default finds {course,_config}.yml, in dir, parents)'
                       )
    args = parser.parse_args()
    if args.out_path is None:
        args.out_path = op.join(args.dir, '..', '..', 'exercises')
    if args.site_config is None:
        args.site_config = find_site_config(args.dir)
    process_dir(args.dir, args.out_path, not args.no_grade, args.site_config)


if __name__ == '__main__':
    main()
