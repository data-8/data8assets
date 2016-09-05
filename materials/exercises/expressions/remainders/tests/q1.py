test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Close.  But 11 isn't the index for a day of the week.
          >>> # Try computing 5 + 34 and *then* taking the remainder of that.
          >>> assignment_day != 11
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assignment_day
          4
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
