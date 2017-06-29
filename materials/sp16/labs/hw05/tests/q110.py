test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> stations_rounded.column('lat,long').item(1) == append_numbers(stations_rounded.column('Rounded Latitude').item(1), stations_rounded.column('Rounded Longitude').item(1))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> coast_distance.column('lat,long').item(1) == append_numbers(coast_distance.column('latitude').item(1), coast_distance.column('longitude').item(1))
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
