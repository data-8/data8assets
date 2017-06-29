test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(spread_for_coastal_and_noncoastal.labels) == 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(spread_for_coastal_and_noncoastal.column(1).item(1) - spread_for_coastal_and_noncoastal.column(1).item(0), 4)
          5.7593
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