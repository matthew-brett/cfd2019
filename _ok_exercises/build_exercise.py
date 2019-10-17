#!/usr/bin/env python
""" Build exercise
"""

import os.path as op
from argparse import ArgumentParser
from subprocess import check_call
from glob import glob
from zipfile import ZipFile

import jupytext
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def read_nb(fname):
    return jupytext.readf(fname)


def clear_directory(fname):
    path = path_of(fname)
    check_call(['git', 'clean', '-fxd', '.'], pwd=path)


def path_of(fname):
    return op.split(op.abspath(fname))[0]


def ipynb_fname(fname):
    froot, ext = op.splitext(fname)
    return froot + '.ipynb'


def execute_nb(nb, path, nbargs=None):
    nbargs = {} if nbargs is None else nbargs
    ep = ExecutePreprocessor(**nbargs)
    ep.preprocess(nb, {'metadata': {'path': path}})
    return nb


def clear_outputs(nb):
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            cell['outputs'] = []
    return nb


def write_nb(nb, fname):
    with open(fname, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)


def pack_exercise(fname):
    path = path_of(fname)
    zip_fname = op.basename(fname) + '.zip'
    files = [f for f in glob(op.join(path, '*')) if not f.endswith('.Rmd')]
    with ZipFile(zip_fname, 'w') as zip_obj:
        for fn in files:
            zip_obj.write(fn)


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('notebook', nargs='+',
                        help='Notebook(s) to clean')
    parser.add_argument('--execute', action='store_true',
                        help='If specified, execute notebooks before cleaning')
    return parser


def process_nb(fname, execute=False):
    clear_directory(fname)
    nb = read_nb(fname)
    if execute:
        nb = execute_nb(nb, path_of(fname))
    nb = clear_outputs(nb)
    write_nb(nb, ipynb_fname(fname))
    pack_exercise(fname)


def main():
    args = get_parser().parse_args()
    for fname in args.notebook:
        process_nb(fname, execute=args.execute)


if __name__ == '__main__':
    main()
