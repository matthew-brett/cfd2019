#!/usr/bin/env python
""" Create default OKpy directory
"""

import os
import os.path as op
from argparse import ArgumentParser


TEMPLATE_OK = '''
{{
  "name": "{name_no_underscores}",
  "src": [
    "{name}.ipynb"
  ],
  "tests": {{
      "tests/q*.py": "ok_test"
  }},
  "protocols": [
      "file_contents",
      "grading",
      "backup"
  ]
}}
'''


def check_out_dir(out_dir):
    if op.exists(out_dir):
        return
    os.makedirs(out_dir)
    tests_dir = op.join(out_dir, 'tests')
    os.makedirs(tests_dir)
    with open(op.join(tests_dir, '__init__.py'), 'wt') as fobj:
        fobj.write('# Init for tests')


def main():
    parser = ArgumentParser()
    parser.add_argument('out_dir', help='Output directory for exercise')
    args = parser.parse_args()
    out_dir = args.out_dir
    check_out_dir(out_dir)
    name = op.basename(out_dir)
    name_no_underscores = name.replace('_', ' ')
    out_fname = op.join(name, f'{name}.ok')
    with open(out_fname, 'wt') as fobj:
        fobj.write(TEMPLATE_OK.format(**locals()))


if __name__ == '__main__':
    main()
