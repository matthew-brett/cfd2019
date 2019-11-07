test = {
  'name': 'Question no_girls',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_no_girls'
          >>> 'p_no_girls' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_no_girls'
          >>> # from its initial state (of ...)
          >>> p_no_girls != ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0.06 < p_no_girls < 0.075
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
