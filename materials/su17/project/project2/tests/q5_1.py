test = {
  'name': 'Question 5.1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> average_murder_rates.labels
          ('Year', 'Death penalty states', 'No death penalty states')
          >>> average_murder_rates.num_rows
          44
          >>> round(average_murder_rates.column(1).item(3), 1) == 4.6
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
