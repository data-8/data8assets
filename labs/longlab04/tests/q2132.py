test = {
  'name': 'Exercise 2.1.3.2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't make a table.  total_pop_by_year
          >>> # should be a table, produced by calling group.  Your code
          >>> # should look something like this:
          >>> #   total_pop_by_year = year_and_population.group(...)
          >>> type(total_pop_by_year)
          <class 'datascience.tables.Table'>
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you didn't group by year.  The table
          >>> # total_pop_by_year should have 44 rows, 1 for each year.
          >>> total_pop_by_year.num_rows
          44
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you didn't aggregate the data for each state in
          >>> # the right way.  2 hints:
          >>> #  * The function sum computes the sum of a bunch of numbers.
          >>> #  * Write something like:
          >>> #      year_and_population.group("Year", ...)
          >>> print(total_pop_by_year.sort("Year").take(np.arange(10)))
          Year | Population sum
          1960 | 178614915
          1961 | 182221000
          1962 | 184935000
          1963 | 187488000
          1964 | 190200000
          1965 | 193013000
          1966 | 195049000
          1967 | 197055000
          1968 | 199051000
          1969 | 201129000
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