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
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
