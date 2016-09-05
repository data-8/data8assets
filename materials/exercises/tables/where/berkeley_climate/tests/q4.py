test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't make a table.
          >>> from datascience import *
          >>> type(with_mile_differences) == tables.Table
          True
          >>> # It looks like the North-South differences aren't correct.
          >>> np.allclose(with_mile_differences.column("North-South difference (miles)") / MILES_PER_DEGREE_LATITUDE, with_degree_differences.column("Latitude difference"))
          True
          >>> # It looks like the East-West differences aren't correct.
          >>> np.allclose(with_mile_differences.column("East-West difference (miles)") / MILES_PER_DEGREE_LONGITUDE, with_degree_differences.column("Longitude difference"))
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
