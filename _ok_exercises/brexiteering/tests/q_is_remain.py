
test = {
  'name': 'Question is_remain',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'is_remain'
          >>> 'is_remain' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'is_remain'
          >>> # from its initial state (of ...)
          >>> is_remain is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # is_remain should be a Boolean series.
          >>> type(is_remain) == pd.Series
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # is_remain should be a Boolean series.
          >>> set(is_remain) == {True, False}
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # is_remain should have True where the vote was equal to 1.
          >>> np.all(is_remain == (good_brexit['cut15'] == 1))
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
