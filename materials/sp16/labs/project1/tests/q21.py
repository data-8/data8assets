test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(per_capita_usage.sort(0).relabeled(1, 'V').take([0, 1, 2]))
          PWSID   | V
          0110001 | 70.7
          0110003 | 90.2727
          0110005 | 76
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> per_capita_usage.num_rows
          411
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
