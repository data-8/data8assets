test = {
  'name': 'Question 4.2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> non_death_penalty_murder_rates.num_rows
          264
          >>> non_death_penalty_murder_rates.labels
          ('State', 'Year', 'Population', 'Murder Rate')
          >>> reject_null_2 in [True, False]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0.25 <= run_test(non_death_penalty_murder_rates, 1971) <= 0.45
          Test statistic 1971 to 1973 : 1
          True
          >>> reject_null_2
          False
          """,
          'hidden': True,
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
