test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You haven't defined a value for n
          >>> 'n' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you didn't use n in your expression for
          >>> # also_roughly_e, or n is not large enough.
          >>> # Hint: Your expression should start like this:
          >>> #   also_roughly_e = (1 + 1/n)...
          >>> round(1 / (also_roughly_e**(1/n) - 1), 2) == round(n, 2)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Your answer looks pretty far off -- maybe you're using the
          >>> # wrong formula?
          >>> round(also_roughly_e, 1)
          2.7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You are close - but it is not close enough yet.
          >>> # Maybe your value for n should be larger?
          >>> round(also_roughly_e, 2)
          2.72
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You are very close - but it is not close enough yet.
          >>> # Maybe your value for n should be larger?
          >>> round(also_roughly_e, 3)
          2.718
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You are very very close - but it is not close enough yet.
          >>> round(also_roughly_e, 4)
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
