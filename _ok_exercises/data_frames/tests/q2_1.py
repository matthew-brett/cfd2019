test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(top_10_movies, pd.DataFrame)
          True
          >>> top_10_movies.sort_values('Name')
             Rating                                               Name
          6     8.9                                12 Angry Men (1957)
          8     8.9             Il buono, il brutto, il cattivo (1966)
          3     8.9                                Pulp Fiction (1994)
          4     8.9                            Schindler's List (1993)
          7     8.9                             The Dark Knight (2008)
          1     9.2                               The Godfather (1972)
          2     9.0                      The Godfather: Part II (1974)
          9     8.8  The Lord of the Rings: The Fellowship of the R...
          5     8.9  The Lord of the Rings: The Return of the King ...
          0     9.2                    The Shawshank Redemption (1994)
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
