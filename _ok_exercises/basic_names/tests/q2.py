test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your answer looks pretty far off -- maybe you're using the
          >>> # wrong formula?
          >>> round(roughly_e, 1)
          2.7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You are close - but it is not close enough yet.
          >>> # Maybe your value for n should be larger?
          >>> round(roughly_e, 2)
          2.72
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You are very close - but it is not close enough yet.
          >>> # Maybe your value for n should be larger?
          >>> round(roughly_e, 3)
          2.718
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You are very very close - but it is not close enough yet.
          >>> # Maybe your value for n should be larger?
          >>> round(roughly_e, 4)
          2.7183
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
