test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(proportions(ratings_by_gender, ['female']))
          Relationship Rating | female | male
          1                   | 61%    | 680
          2                   | 31%    | 284
          3                   | 3%     | 31
          4                   | 3%     | 33
          5                   | 2%     | 5
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
