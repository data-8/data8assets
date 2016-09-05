test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't make a map.  Your code should
          >>> # look something like this:
          >>> #   us_map = Map.read_geojson(...)
          >>> from datascience import *
          >>> type(us_map) == maps.Map
          True
          >>> us_map.features[0]['NAME']
          'Alaska'
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
