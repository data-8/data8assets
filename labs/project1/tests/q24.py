test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(district_data) == Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(district_data.sort(0).take([0, 1, 2]))
          PWSID   | Population    | Water      | Income
          0110001 | 3,397,562.00  | 7,204.45   | 79,031.97
          0110005 | 15,115,000.00 | 34,344.42  | 82,497.18
          0110006 | 1,661,407.00  | 2,850.07   | 52,923.52
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
