test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(zero_wait, 4) == 33.4744
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(two_minutes_wait, 4) == 54.9337
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(hour_wait, 4) == 677.2529
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
