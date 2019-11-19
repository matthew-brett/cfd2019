
test = {
  'name': 'Question 1_money_death',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'money_death'
          >>> 'money_death' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'money_death'
          >>> # from its initial state (of ...)
          >>> money_death is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # money_death should be a data frame.
          >>> isinstance(money_death, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Your column names don't look right.
          >>> sorted(money_death) == ["DeathPenalty", "Income"]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(money_death) == len(gss)
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
