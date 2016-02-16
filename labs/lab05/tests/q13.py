test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(float(average_age), 2) == 26.54
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(float(average_salary), 2) == 4269775.77
          True
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
