#!/usr/bin/env python
""" Check that marks noted in Rmd correspond to OKpy points
"""

import os.path as op
from glob import glob
import re
from argparse import ArgumentParser

from rnbgrader import loads
from rmdex.exerciser import read_utf8, question_chunks, get_marks


GRADE_RE = re.compile(r"""\.\s*grade\s*\(\s*['"](.*?)['"]\s*\)""")

# For tests
HERE = op.dirname(__file__)
NB_DIR = op.join(HERE, 'tests', 'data', 'three_girls')
TESTS = sorted(glob(op.join(NB_DIR, 'tests', 'q*.py')))


def ok_test_name(code):
    match = GRADE_RE.search(code)
    return None if match is None else match.groups()[0]


def load_test(test_fname):
    ns = {}
    with open(test_fname, 'rt') as fobj:
        exec(fobj.read(), ns)
    assert 'test' in ns
    return ns['test']


def check_points(rmd_fname, tests_path=None):
    if tests_path is None:
        tests_path = op.join(op.dirname(rmd_fname), 'tests')
    # Find chunks
    nb = loads(read_utf8(rmd_fname))
    chunks = nb.chunks
    # Identify questions
    questions = question_chunks(nb)
    for question in questions[:-1]:
        # Find following ok.grade chunk, if present.
        q_i = chunks.index(question)
        assert q_i >= 0
        test_name = ok_test_name(chunks[q_i + 1].code)
        if test_name is None:
            continue
        # Get marks allocated
        marks, out_of, running_total = get_marks(question.code)
        # Load corresponding test
        test = load_test(op.join(tests_path, test_name + '.py'))
        # Check points same as marks allocated
        assert test['points'] == float(marks)


def test_ok_test_name():
    assert ok_test_name('ok.grade("foo")') == 'foo'
    assert ok_test_name('# A comment\nnb.grade("funny file")') == 'funny file'
    assert ok_test_name('# Three\nnb. grade (  "funny file" )  # Comments\n'
                        '# Here') == 'funny file'


def test_smoke():
    rmd_fname = op.join(NB_DIR, 'three_girls_template.Rmd')
    check_points(rmd_fname)


def get_args():
    parser = ArgumentParser(__doc__)
    parser.add_argument('rmd_fname', help='Path to Rmd notebook')
    parser.add_argument('--tests-path',
                        help='Path to notebook test directory'
                       'default is "tests" directory in path of notebook(s)')
    args = parser.parse_args()
    if args.tests_path is None:
        args.tests_path = op.join(op.dirname(args.rmd_fname), 'tests')
    return args


def main():
    args = get_args()
    check_points(args.rmd_fname, args.tests_path)


if __name__ == '__main__':
    main()
