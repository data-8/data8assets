test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(float(small_stats[0]), 2) == 26.32
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(float(small_stats[1]), 2) == 4283910.89
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(float(large_stats[0]), 2) == 26.42
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(float(large_stats[1]), 2) == 4821322.5
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
