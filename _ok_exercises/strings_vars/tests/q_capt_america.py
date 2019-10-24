test = {
  'name': '_capt_marvel',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # another_character.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell where you defined
          >>> # another_character.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'another_character' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You've defined another_character, but it is not a string.
          >>> type(another_character) == str
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You've defined another_character, and it is a string, but its not
          >>> # right yet.  Have you got the spaces and capital letters right?
          >>> another_character == "Captain America"
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
