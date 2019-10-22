test = {
  'name': '_marvel',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # person.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell where you defined
          >>> # person.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'person' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you didn't change the cell to define
          >>> # person appropriately.  It should be a string.
          >>> person != ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You've defined person, but it is not a string.
          >>> # For example, this is almost right:
          >>> # person = "marvel"
          >>> type(person) == str
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You've defined person, but the value has a space at
          >>> # the end.
          >>> person.endswith(' ')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You've defined person, and it is a string, but its not
          >>> # right yet.  Here's the example that is almost right:
          >>> # person = "marvel"
          >>> person == "Marvel"
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
