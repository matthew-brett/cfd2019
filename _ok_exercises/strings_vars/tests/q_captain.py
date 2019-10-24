test = {
  'name': '_captain',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # title.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell where you defined
          >>> # title.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'title' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you didn't change the cell to define
          >>> # title appropriately.  It should be a string.
          >>> title != ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You've defined title, but it is not a string.
          >>> # For example, this is almost right:
          >>> # title = "captain"
          >>> type(title) == str
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You've defined title, but it does not have a space at
          >>> # the end. For example, this is almost right:
          >>> # title = "captain "
          >>> title.endswith(' ')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You've defined title, and it is a string, but its not
          >>> # right yet.  Here's the example that is almost right:
          >>> # title = "captain "
          >>> title == "Captain "
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
