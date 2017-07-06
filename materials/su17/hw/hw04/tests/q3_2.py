test = {
  'name': 'Question 3_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> get_day_in_month(315)
          15
          >>> get_day_in_month(922)
          22
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> [get_day_in_month(k) for k in range(111, 333, 7) if 0 < k % 100 < 32]
          [11, 18, 25, 2, 9, 16, 23, 30, 7, 14, 21, 28]
          """,
          'hidden': True,
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
