test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # We're asking for the number of *pieces* of fruit, not the
          >>> # number of kinds of fruit or the number of boxes from which
          >>> # there were sales.
          >>> total_fruits_sold > 10
          True
          >>> total_fruits_sold
          638
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
