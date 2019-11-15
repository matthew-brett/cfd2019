
test = {
  'name': 'Question leavers',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'leavers'
          >>> 'leavers' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'leavers'
          >>> # from its initial state (of ...)
          >>> leavers is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # leavers should be a data frame
          >>> type(leavers) == pd.DataFrame
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # leavers should have as many rows as there cut15 values of 2.
          >>> len(leavers) == np.count_nonzero(good_brexit['cut15'] == 2)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # leavers 'cut15' should all be equal to 2.
          >>> np.all(leavers['cut15'] == 2)
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
