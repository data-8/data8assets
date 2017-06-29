test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> alpha_column(final).item(0)
          84.76
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(alpha_column(Table().with_columns(['a', [1], 'b', [2]])))
          [1]
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
