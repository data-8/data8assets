test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 'distance to coast (km)' in daily_temp_with_distances.labels
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> daily_temp_with_distances.labels[1] == 'Tmax'
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> daily_temp_with_distances.column(0).item(0)
          130
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
