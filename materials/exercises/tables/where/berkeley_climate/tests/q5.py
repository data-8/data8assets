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
          >>> type(with_distances) == tables.Table
          True
          >>> with_distances.select("Station name", "Distance to UC Berkeley").group("Station name", np.mean).sort("Station name").take(range(5))
          Station name  | Distance to UC Berkeley mean
          Alturas       | 266.343
          Arcata/Eureka | 236.935
          Avalon        | 372.858
          Bakersfield   | 242.699
          Bishop        | 215.779
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
