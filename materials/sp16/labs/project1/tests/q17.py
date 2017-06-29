test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(high_average_zips.sort('ZIP').take([0, 1, 2]).select('ZIP'))
          ZIP
          90010
          90024
          90025
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
