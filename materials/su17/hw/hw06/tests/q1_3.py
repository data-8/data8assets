test = {
  'name': 'Question 1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> -1 <= diff_lower_bound <= diff_upper_bound <= 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> -0.05 <= diff_lower_bound <= diff_upper_bound <= 0.2
          True
          >>> diff_lower_bound - diff_upper_bound < -0.1
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
