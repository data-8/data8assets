test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> -1 <= simulate_statistic_under_null(1) <= 1
          True
          >>> -1 <= simulate_statistic_under_null(1) <= 1
          True
          >>> -1 <= simulate_statistic_under_null(1) <= 1
          True
          >>> -150 <= simulate_statistic_under_null(1000) <= 150
          True
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
