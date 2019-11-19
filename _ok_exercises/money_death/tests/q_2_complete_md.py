
test = {
  'name': 'Question 2_complete_md',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'complete_md'
          >>> 'complete_md' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'complete_md'
          >>> # from its initial state (of ...)
          >>> complete_md is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Wrong number of rows - did you drop the NaN values?
          >>> complete_md.shape == (904, 2)
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
