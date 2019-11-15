
test = {
  'name': 'Question remainers',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'remainers'
          >>> 'remainers' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'remainers'
          >>> # from its initial state (of ...)
          >>> remainers is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # remainers should be a data frame
          >>> type(remainers) == pd.DataFrame
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # remainers should have as many rows as there cut15 values of 1.
          >>> len(remainers) == np.count_nonzero(good_brexit['cut15'] == 1)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # remainers 'cut15' should all be equal to 1.
          >>> np.all(remainers['cut15'] == 1)
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
