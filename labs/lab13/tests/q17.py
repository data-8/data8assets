test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(new_two_minutes_wait, 2) == 54.93
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(fitted_value(faithful, 'eruptions', 'waiting', 10), 4) == 140.7708
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
