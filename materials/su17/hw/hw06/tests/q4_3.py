test = {
  'name': 'Question 4_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> exact_sd < 0.05
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0.02 <= exact_sd <= 0.03
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
