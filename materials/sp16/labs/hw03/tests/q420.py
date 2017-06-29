test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> table_shape(Table().with_columns(['a', [1], 'b', [2]]))
          'wide'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> table_shape(Table().with_columns(['a', [1, 2, 3], 'b', [4, 5, 6]]))
          'tall'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> table_shape(Table().with_columns(['a', [1, 2], 'b', [4, 5]]))
          'square'
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
