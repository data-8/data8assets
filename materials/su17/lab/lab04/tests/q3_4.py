test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(cash_proportion) == 102
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import math
          >>> math.isclose(cash_proportion.item(0), 0.01784038, rel_tol = .001)
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
