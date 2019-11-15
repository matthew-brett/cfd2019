
test = {
  'name': 'Question age_not_0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'age_not_0'
          >>> 'age_not_0' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'age_not_0'
          >>> # from its initial state (of ...)
          >>> age_not_0 is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # age_not_0 should be same length as the ages series.
          >>> len(age_not_0) == len(ages)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # age_not_0 should contain only True and False values.
          >>> set(age_not_0) == {True, False}
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # There should be 14 False values.  Did you use != ?
          >>> np.count_nonzero(age_not_0 == False) == 14
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
