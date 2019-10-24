""" Helpers for notebook tests
"""

import re
import io
import sys


def find_inputs(defined):
    return {n: v for n, v in defined.items() if re.match('_i\d+$', n)}


def find_outputs(defined):
    return {n: v for n, v in defined.items() if re.match('_\d+$', n)}


def filter_values(inputs, regex):
    regex = re.compile(regex)
    return {n: v for n, v in inputs.items() if regex.search(v)}


def get_print_inputs(defined):
    cells = find_inputs(defined)
    return list(filter_values(cells, r'print\s*\(').values())


def get_print_outputs(defined, strip_ws=True):
    outputs = []
    # Redirect stdout when running print cells.
    sys_start = sys.stdout
    for v in get_print_inputs(defined):
        s = io.StringIO()
        sys.stdout = s
        try:
            # Work out safe way of doing deeper copy?
            exec(v, defined.copy())
        except:
            pass
        output = s.getvalue()
        if output:
            if strip_ws:
                output = '\n'.join([L.strip() for L in output.splitlines()])
            outputs.append(output)
    sys.stdout = sys_start
    return outputs


def _right_start(output, start):
    lines = output.splitlines()
    return len(lines) and lines[0].startswith(start)


def _has_n_lines(output, n):
    return len(output.splitlines()) == n


def corresponding_in_name(out_name):
    assert out_name.startswith('_')
    return f'_i{out_name[1:]}'


class QInt:

    exp_value = int
    calc_regex = re.compile(r'\s*type\s*\(\s*a\s*\)')

    def __init__(self, defined):
        self.defined = defined.copy()

    def right_value(self):
        outputs = find_outputs(self.defined)
        return self.exp_value in outputs.values()

    def right_calculation(self):
        outputs = find_outputs(self.defined)
        good_out_names = [n for n, v in outputs.items() if v == self.exp_value]
        good_ins = [self.defined[corresponding_in_name(n)] for n in
                    good_out_names]
        return len([i for i in good_ins if self.calc_regex.search(i)]) > 0


class QFloat(QInt):

    exp_value = float
    calc_regex = re.compile(r'\s*type\s*\(\s*b\s*\)')


class QString(QInt):

    exp_value = str
    calc_regex = re.compile(r'\s*type\s*\(\s*c\s*\)')
