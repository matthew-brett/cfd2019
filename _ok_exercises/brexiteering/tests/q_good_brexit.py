
test = {
  'name': 'Question good_brexit',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'good_brexit'
          >>> 'good_brexit' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'good_brexit'
          >>> # from its initial state (of ...)
          >>> good_brexit is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # good_brexit should be a data frame
          >>> type(good_brexit) == pd.DataFrame
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # good_brexit should have 14 fewer rows than mini_brexit
          >>> len(good_brexit) == len(mini_brexit) - 14
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
