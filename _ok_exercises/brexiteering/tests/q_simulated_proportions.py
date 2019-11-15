
test = {
  'name': 'Question simulated_proportions',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'simulated_proportions'
          >>> 'simulated_proportions' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'simulated_proportions'
          >>> # from its initial state (of ...)
          >>> simulated_proportions is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # simulated_proportions should have 10000 values
          >>> len(simulated_proportions) == 10000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # simulated_proportions values should be proportions
          >>> np.all(np.logical_and(
          ...     simulated_proportions >= 0,
          ...     simulated_proportions <= 1))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          # n = 1000
          # samps = np.random.binomial
          'code': r"""
          >>> # simulated_proportions values should be between 0.44 and 0.6
          >>> np.all(np.logical_and(
          ...     simulated_proportions >= 0.44,
          ...     simulated_proportions <= 0.6))
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
