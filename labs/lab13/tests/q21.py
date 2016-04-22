test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 10.7 < np.mean(regression_lines['slope']) < 10.8
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 33.4 < np.mean(regression_lines['intercept']) < 33.6
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
