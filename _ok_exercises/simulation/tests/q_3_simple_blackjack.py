
test = {
  'name': 'Question 3_simple_blackjack',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_total_21'
          >>> 'p_total_21' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_total_21'
          >>> # from its initial state (of ...)
          >>> p_total_21 != ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          # n = 10000
          # ranks = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
          # results = np.random.multinomial(3, np.ones(13) / 13, n * n)
          # scores = results @ ranks
          # per_n = (scores == 21).reshape((n, n)).sum(axis=1) / n
          # np.quantile(per_n , [0.001, 0.999])
          'code': r"""
          >>> 0.07 < p_total_21 < 0.875
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
