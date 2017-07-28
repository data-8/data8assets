test = {
  'name': 'Question 2_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Check your column labels and spelling
          >>> largest.labels == ('name', 'poverty_total')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # India is the country with the largest number of people living
          >>> # in extreme poverty.
          >>> largest.column(0).item(0)
          'India'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The table should contain exactly 10 rows.
          >>> largest.num_rows
          10
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
