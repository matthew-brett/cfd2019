test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(imdb_by_year) == pd.DataFrame
          True
          >>> list(imdb_by_year['Title'].iloc[:3])
          ['The Kid', 'The Gold Rush', 'The General']
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
