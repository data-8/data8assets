test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(daily_temp) == Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(stations) == Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(stations.labels) == 15
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(coast_distance) == Table
          True
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