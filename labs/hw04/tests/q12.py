test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> quoted_number_to_int("'5'")
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> quoted_number_to_int("'-10'")
          -10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> quoted_number_to_int("'0010'")
          10
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
