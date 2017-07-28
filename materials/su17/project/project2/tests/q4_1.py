test = {
  'name': 'Question 4.1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0.0 <= run_test(death_penalty_murder_rates, 1960) <= 0.12
          Test statistic 1960 to 1962 : -9
          True
          >>> 0.0 <= run_test(murder_rates, 1960) <= 0.05
          Test statistic 1960 to 1962 : -13
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
