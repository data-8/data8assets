test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Close.  But 29 isn't an hour of the day.  It's a
          >>> # whole day, plus 5 hours...
          >>> assignment_hour != 29
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assignment_hour
          6
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
