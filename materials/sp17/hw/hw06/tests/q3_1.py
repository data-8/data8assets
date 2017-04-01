test = {
  'name': 'Question 3_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> example = Table().with_columns('age', [0, 1, 2, 3, 5, 6], 'count', [2, 5, 1, 4, 10, 1])
          >>> example2 = Table().with_columns('age', [10, 11, 12, 23, 25, 26], 'count', [2, 5, 1, 4, 10, 1])
          >>> 1 <= grouped_mean(example) <= 5
          True
          >>> 11 <= grouped_mean(example2) <= 25
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
