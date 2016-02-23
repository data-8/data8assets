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
          0110001 | 5.80953
          0110003 | 7.40036
          0110005 | 6.22523
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
