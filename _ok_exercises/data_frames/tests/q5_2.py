test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(ninety_nine) == 5
          True
          >>> ninety_nine.sort_values('Votes')
                 Votes  Rating            Title  Year  Decade
          115   630994     8.1  The Sixth Sense  1999    1990
          149   672878     8.5   The Green Mile  1999    1990
          104   735056     8.4  American Beauty  1999    1990
          129  1073043     8.7       The Matrix  1999    1990
          87   1177098     8.8       Fight Club  1999    1990
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
