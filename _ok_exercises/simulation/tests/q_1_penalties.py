
test = {
  'name': 'Question 1_penalties',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_15_of_15'
          >>> 'p_15_of_15' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_15_of_15'
          >>> # from its initial state (of ...)
          >>> p_15_of_15 != ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          # n = 10000
          # # Take 10000 samples of 10000 trials of this problem.
          # res = np.sum(np.random.binomial(15, 0.8, (n, n)) == 0, axis=1) / n
          # np.quantile(res, [0.001, 0.999])
          'code': r"""
          >>> 0.029 < p_15_of_15 < 0.041
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
