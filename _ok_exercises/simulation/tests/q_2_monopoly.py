
test = {
  'name': 'Question 2_monopoly',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_10_or_more'
          >>> 'p_10_or_more' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_10_or_more'
          >>> # from its initial state (of ...)
          >>> p_10_or_more != ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          # n = 10000
          # results = np.random.multinomial(2, np.ones(6) / 6, n * n)
          # scores = results @ np.arange(1, 7)
          # per_n = (scores >= 10).reshape((n, n)).sum(axis=1) / n
          # np.quantile(per_n , [0.001, 0.999])
          'code': r"""
          >>> 0.154 < p_10_or_more < 0.179
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
