test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> B.all_columns_equal(medium_counts, q15ans)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': 'import tests.build_answers as B\n'+
               'q15ans = B.q15answer()',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
