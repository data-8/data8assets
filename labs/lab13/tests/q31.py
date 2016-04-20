test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 9.85 < slope_interval[0] < 10
          True
          """,
          'hidden': False,
          'locked': False
        }, 
        {
          'code': r"""
          >>> 11 < slope_interval[1] < 11.7
          True
          """,
          'hidden': False,
          'locked': False
        }
                
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
