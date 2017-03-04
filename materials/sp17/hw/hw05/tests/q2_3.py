test = {
  'name': 'Question 2_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your test statistic does not distinguish between ordinary landings and unusual positions. Try another one.
          >>> 0 < landing_test_statistic(80, 30)
          True
          >>> normal = [landing_test_statistic(x, y) for x in np.arange(-40, 40, 3) for y in np.arange(-40, 40, 3)]
          >>> min(normal) <= landing_test_statistic(80, 30) <= max(normal)
          False
          >>> min(normal) <= landing_test_statistic(-80, 30) <= max(normal)
          False
          >>> min(normal) <= landing_test_statistic(80, -30) <= max(normal)
          False
          >>> min(normal) <= landing_test_statistic(-80, -30) <= max(normal)
          False
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
