test = {
  'name': 'Question 1_12',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Check your column labels and spelling
          >>> pop_by_decade.labels == ('decade', 'population')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The first year of the 1960's is 1960.
          >>> pop_by_decade.column(0).item(0) == 1960
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
