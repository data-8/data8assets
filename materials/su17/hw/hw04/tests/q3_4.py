test = {
  'name': 'Question 3_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 60 < thanksgiving_prediction < 70
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(thanksgiving_prediction, 2) == 64.32
          True
          """,
          'hidden': True,
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
