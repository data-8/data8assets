test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(convenience_stats)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(float(convenience_stats[0]), 2) == 20.36
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(float(convenience_stats[1]), 2) == 2383533.82
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
