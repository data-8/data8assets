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
          PWSID   | Population | Water | Income
          0110001 | 340,000    | 71    | 79,032
          0110005 | 1,390,000  | 76    | 82,497
          0110006 | 151,037    | 57    | 52,924
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
