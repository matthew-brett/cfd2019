
test = {
  'name': 'Question is_leave',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'is_leave'
          >>> 'is_leave' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'is_leave'
          >>> # from its initial state (of ...)
          >>> is_leave is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # is_leave should be a Boolean series.
          >>> type(is_leave) == pd.Series
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # is_leave should be a Boolean series.
          >>> set(is_leave) == {True, False}
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # is_leave should have True where the vote was equal to 2.
          >>> np.all(is_leave == (good_brexit['cut15'] == 2))
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
