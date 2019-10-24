test = {
  'name': '_capt_marvel',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # character.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell where you defined
          >>> # character.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'character' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you didn't change the cell to define
          >>> # character appropriately.  It should be a string.
          >>> character != ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You've defined character, but it is not a string.
          >>> type(character) == str
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You've defined character, but the value has a space at
          >>> # the end.
          >>> character.endswith(' ')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You've defined character, and it is a string, but its not
          >>> # right yet.  Here's the example that is almost right:
          >>> # character = title and person
          >>> character == "Captain Marvel"
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
