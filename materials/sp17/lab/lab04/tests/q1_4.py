test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> convert_pay_string_to_number("$100 ") == 100000000.0
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> convert_pay_string_to_number("$23 ") == 23000000.0
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
