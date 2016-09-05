test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> closest_station_readings.take(range(5))
          Highest temp that day (F) | Lowest temp that day (F) | Date | Latitude | Longitude | Station name
          63                        | 46                       | 109  | 37.7214  | -122.221  | Oakland
          58                        | 45                       | 120  | 37.7214  | -122.221  | Oakland
          61                        | 40                       | 121  | 37.7214  | -122.221  | Oakland
          64                        | 39                       | 123  | 37.7214  | -122.221  | Oakland
          69                        | 46                       | 124  | 37.7214  | -122.221  | Oakland
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
