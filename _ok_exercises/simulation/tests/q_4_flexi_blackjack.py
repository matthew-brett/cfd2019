
test = {
  'name': 'Question 4_flexi_blackjack',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_flex_total_21'
          >>> 'p_flex_total_21' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_flex_total_21'
          >>> # from its initial state (of ...)
          >>> p_flex_total_21 != ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          # n = 10000
          # ranks = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
          # results = np.random.multinomial(3, np.ones(13) / 13, n * n)
          # scores1 = results @ ranks
          # # Add 10 for aces.
          # scores11 = scores1 + results[:, 0] * 10
          # True if ace=1 or ace=11 generates 21.
          # scores_21 = np.any(np.c_[scores1, scores11] == 21, axis=1)
          # per_n = scores_21.reshape((n, n)).sum(axis=1) / n
          # np.quantile(per_n , [0.001, 0.999])
          'code': r"""
          >>> 0.079 < p_flex_total_21 < 0.0971
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
