#!/usr/bin/env python
""" Create default OKpy question
"""

import os
import os.path as op
from argparse import ArgumentParser


TEMPLATE_Q = '''
test = {{
  'name': 'Question {q_name}',
  'points': 1,
  'suites': [
    {{
      'cases': [
        {{
          'code': r"""
          >>> # You need to set the value for '{v_name}'
          >>> '{v_name}' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        }},
        {{
          'code': r"""
          >>> # You haven't changed the value for '{v_name}'
          >>> # from its initial state (of ...)
          >>> {v_name} is not ...
          True
          """,
          'hidden': False,
          'locked': False
        }},
        {{
          'code': r"""
          >>> False
          True
          """,
          'hidden': False,
          'locked': False
        }},
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }}
  ]
}}
'''


def check_out_dir(out_dir):
    if not op.exists(out_dir):
        os.makedirs(out_dir)
        with open(op.join(out_dir, '__init__.py'), 'wt') as fobj:
            fobj.write('# Init for tests')


def main():
    parser = ArgumentParser()
    parser.add_argument('v_name', help='variable name')
    parser.add_argument('q_name', nargs='?', help='question name')
    parser.add_argument('--out-dir', default=op.join(os.getcwd(), 'tests'),
                        help='output directory')
    args = parser.parse_args()
    v_name = args.v_name
    q_name = v_name if args.q_name is None else args.q_name
    out_dir = args.out_dir
    check_out_dir(out_dir)
    out_fname = op.join(out_dir, f'q_{q_name}.py')
    with open(out_fname, 'wt') as fobj:
        fobj.write(TEMPLATE_Q.format(**locals()))


if __name__ == '__main__':
    main()
