test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> stations_rounded.column('Rounded Latitude').item(1) == mysterious_function(stations_rounded.column('Latitude').item(1))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> stations_rounded.column('Rounded Longitude').item(1) == mysterious_function(stations_rounded.column('Longitude').item(1))
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
