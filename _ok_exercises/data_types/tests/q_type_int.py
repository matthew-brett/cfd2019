test = {
  'name': '_type_int',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You don't have the right value yet.  Keep trying...
          >>> th.QInt(vars()).right_value()
          True
          """,
          'hidden': True,
          'locked': False
        },
        {
          'code': r"""
          >>> # You have the right value, but your calculation should
          >>> # use the "type" function
          >>> th.QInt(vars()).right_calculation()
          True
          """,
          'hidden': True,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import tests.helpers as th
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
