test = {
  'name': 'Exercise 2.2.1.2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You should find 22 such rows.
          >>> high_murder_rates.num_rows
          22
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # For the predicate, try:
          >>> #   are.above(16.5)
          >>> print(high_murder_rates.sort("State").take(np.arange(10)))
          State     | Year | Population | Murder Rate
          Alaska    | 1982 | 438,000    | 18.5
          Georgia   | 1972 | 4,720,000  | 18.5
          Georgia   | 1973 | 4,786,000  | 17.4
          Georgia   | 1974 | 4,882,000  | 17.8
          Georgia   | 1979 | 5,118,000  | 17.1
          Georgia   | 1981 | 5,569,000  | 17.2
          Louisiana | 1979 | 4,026,000  | 16.9
          Louisiana | 1990 | 4,219,973  | 17.2
          Louisiana | 1991 | 4,252,000  | 16.9
          Louisiana | 1992 | 4,287,000  | 17.4
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