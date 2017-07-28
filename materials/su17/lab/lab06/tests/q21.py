test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(float(compute_statistics(full_data)[0]), 2) == 26.54
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(float(compute_statistics(full_data)[1]), 2) == 4269775.77
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
