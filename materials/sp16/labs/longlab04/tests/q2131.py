test = {
  'name': 'Exercise 2.1.3.1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't make a table.  num_states_by_year
          >>> # should be a table, produced by calling group.  Your code
          >>> # should look something like this:
          >>> #   num_states_by_year = murder_rates.group(...)
          >>> type(num_states_by_year)
          <class 'datascience.tables.Table'>
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you didn't group by year.  The table
          >>> # num_states_by_year should have 44 rows, 1 for each year.
          >>> num_states_by_year.num_rows
          44
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(num_states_by_year.sort("Year").take(np.arange(10)))
          Year | count
          1960 | 50
          1961 | 50
          1962 | 50
          1963 | 50
          1964 | 50
          1965 | 50
          1966 | 50
          1967 | 50
          1968 | 50
          1969 | 50
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