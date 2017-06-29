test = {
  'name': 'Exercise 2.2.1.1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't make a table.  murder_rates_1960
          >>> # should be a table, produced by calling where.  Your code
          >>> # should look something like this:
          >>> #   murder_rates_1960 = murder_rates.where(...)
          >>> type(murder_rates_1960)
          <class 'datascience.tables.Table'>
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you didn't select just one year.  The table
          >>> # murder_rates_1960 should have 50 rows, 1 for each state.
          >>> # 
          >>> # Or maybe you wrote something like:
          >>> #   murder_rates.where("Year", are.equal_to("1960"))
          >>> # The problem is that the years are numbers, not strings, so you
          >>> # need to say instead:
          >>> #   murder_rates.where("Year", are.equal_to(1960))
          >>> murder_rates_1960.num_rows
          50
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you didn't choose the right year.  Write
          >>> # something like:
          >>> #      murder_rates.where("Year", are.equal_to(1960))
          >>> print(murder_rates_1960.sort("State").take(np.arange(10)))
          State       | Year | Population | Murder Rate
          Alabama     | 1960 | 3,266,740  | 12.4
          Alaska      | 1960 | 226,167    | 10.2
          Arizona     | 1960 | 1,302,161  | 6
          Arkansas    | 1960 | 1,786,272  | 8.5
          California  | 1960 | 15,717,204 | 3.9
          Colorado    | 1960 | 1,753,947  | 4.2
          Connecticut | 1960 | 2,535,234  | 1.6
          Delaware    | 1960 | 446,292    | 7.4
          Florida     | 1960 | 4,951,560  | 10.6
          Georgia     | 1960 | 3,943,116  | 11.9
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