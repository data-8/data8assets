test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> with_siblings.num_columns
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(with_siblings.column('# Siblings'))
          [2, 1, 1, 1, 1]
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
