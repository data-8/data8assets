test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure to remove the "(No previous year)" CEOs 
          >>> "(No previous year)" not in with_previous_compensation.column("% Change")
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import math
          >>> # You have the column, but some of your values may be wrong
          >>> t = with_previous_compensation.sort("2014 Total Pay ($)", descending = True)
          >>> value = t.column("2014 Total Pay ($)").item(0)
          >>> math.isclose(value, 67700000.0, rel_tol = 1000)
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You have the column, but your number of rows is off
          >>> with_previous_compensation.num_rows == 81
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
