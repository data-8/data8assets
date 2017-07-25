test = {
  'name': 'Question 3_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 30 <= empirical_sd(1) <= 50
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 10 <= empirical_sd(10) <= 15
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
