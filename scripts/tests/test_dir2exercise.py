# Test for dir2exercise utilities

import os.path as op
import sys

HERE = op.realpath(op.dirname(__file__))
sys.path.append(op.join(HERE, '..'))
DATA_DIR = op.join(HERE, 'data')


from tempfile import TemporaryDirectory
from dir2exercise import find_site_config, get_site_dict


def test_find_site_config():
    with TemporaryDirectory() as tmpdir:
        assert find_site_config(tmpdir) is None
    # Finding _config.yml in main repo directory.
    assert find_site_config('.') == op.realpath(op.join('..', '_config.yml'))
    # Check prefer course.yml to _config.yml
    exp_fn = op.realpath(op.join(DATA_DIR, 'course.yml'))
    assert find_site_config(DATA_DIR) == exp_fn
    # Starting at an empty directory finds one dir below.
    assert find_site_config(op.join(DATA_DIR, 'empty_dir')) == exp_fn
    # Single config in directory.
    ed_pth = op.join(DATA_DIR, 'exercise_dir')
    assert find_site_config(ed_pth) == op.join(ed_pth, '_config.yml')


def test_get_site_dict():
    # Check prefer course.yml to _config.yml
    fn1 = op.realpath(op.join(DATA_DIR, 'course.yml'))
    assert get_site_dict(fn1) == {'baseurl': 'https://foo.github.com/bar',
                                  'baz': 'bong'}
    fn2 = op.realpath(op.join(DATA_DIR, '_config.yml'))
    assert get_site_dict(fn2) == {
        'baseurl': 'https://matthew-brett.github.io/cfd2019'}
