
test = {
  'name': 'Question votes',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'votes'
          >>> 'votes' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'votes'
          >>> # from its initial state (of ...)
          >>> votes is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # votes should be a series
          >>> type(votes) == pd.Series
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # votes should have the values from cut15 good_brexit column.
          >>> np.all(votes == good_brexit['cut15'])
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
