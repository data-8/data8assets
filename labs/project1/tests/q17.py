test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(high_average_zips.sort(0).take([0, 1, 2]))
          ZIP   | Average Income
          90010 | 145010
          90024 | 299216
          90025 | 160059
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> high_average_zips.num_rows
          238
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
