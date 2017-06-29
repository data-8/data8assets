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
        },
        {
          'code': r"""
          >>> print(largest.take(np.arange(3)).column(1))
          [  2.90881638e+08   9.88911670e+07   8.39446430e+07]
          """,
          'hidden': True,
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
