test = {
  'name': '_peggy_carter',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # third_character.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell where you defined
          >>> # third_character.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'third_character' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You've defined third_character, but it is not a string.
          >>> type(third_character) == str
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You've defined third_character, and it is a string, but its not
          >>> # right yet.  Have you got the spaces and capital letters right?
          >>> third_character == "Peggy Carter"
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
