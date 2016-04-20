test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pi1 = prediction_interval(1)
          >>> 42 < pi1[0] < 43
          True
          >>> 45 < pi1[1] < 46
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> pi5 = prediction_interval(5)
          >>> 85.5 < pi5[0] < 86.5
          True
          >>> 88 < pi5[1] < 89
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
