test = {
  'name': '3.2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # seconds_in_a_decade.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell below Question 3.2 where you defined
          >>> # seconds_in_a_decade.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'seconds_in_a_decade' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you didn't change the cell to define
          >>> # seconds_in_a_decade appropriately.  It should be a number,
          >>> # computed using Python's arithmetic.  For example, this is
          >>> # almost right:
          >>> #   seconds_in_a_decade = 10*365*24*60*60
          >>> seconds_in_a_decade != ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you didn't account for leap years.
          >>> # There were 2 leap years and 8 non-leap years in this period.
          >>> # Leap years have 366 days instead of 365.
          >>> seconds_in_a_decade != 315360000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> seconds_in_a_decade == 315532800
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
