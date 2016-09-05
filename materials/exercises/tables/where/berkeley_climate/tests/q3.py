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
          >>> type(with_degree_differences) == tables.Table
          True
          >>> # It looks like the latitude differences aren't correct.
          >>> all(with_degree_differences.column("Latitude difference") + BERKELEY_LATITUDE == temperatures.column("Latitude"))
          True
          >>> # It looks like you subtracted UC Berkeley's latitude from all
          >>> # the longitudes.
          >>> not all(with_degree_differences.column("Longitude difference") + BERKELEY_LATITUDE == temperatures.column("Longitude"))
          True
          >>> # It looks like the longitude differences aren't correct.
          >>> all(with_degree_differences.column("Longitude difference") + BERKELEY_LONGITUDE == temperatures.column("Longitude"))
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
