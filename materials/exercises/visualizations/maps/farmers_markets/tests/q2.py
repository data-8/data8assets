test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you switched latitude and longitude.
          >>> round(np.mean([v.lat_lon[1] for v in simple_map.values() if not np.isnan(v.lat_lon[0])]), 3) != 36.552
          True
          >>> # The average location of the markers isn't what we expected.
          >>> round(np.mean([v.lat_lon[0] for v in simple_map.values() if not np.isnan(v.lat_lon[0])]), 3) == 36.552
          True
          >>> round(np.mean([v.lat_lon[1] for v in simple_map.values() if not np.isnan(v.lat_lon[0])]), 3) == -120.262
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
