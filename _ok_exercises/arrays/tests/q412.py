test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(interesting_numbers) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(interesting_numbers)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> all(interesting_numbers == np.array([0, 1, -1, np.pi, np.e]))
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
