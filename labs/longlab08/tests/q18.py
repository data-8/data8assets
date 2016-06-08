test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> B.all_columns_equal(clean_medium_max, q16ans)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': 'import tests.build_answers as B\n'+
               'q16ans = B.q16answer()',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
