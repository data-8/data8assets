test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(stations_with_distances.labels) == 21
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> stations_with_distances.labels[1] == 'WBAN'
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> stations_with_distances.column(0).item(3)
          '-7.5,72.5'
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