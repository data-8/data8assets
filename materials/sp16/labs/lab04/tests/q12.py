test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> B.all_columns_equal(superstars, q12ans)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': 'import tests.build_answers as B\n' +
               'q12ans = B.q12answer1()',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
