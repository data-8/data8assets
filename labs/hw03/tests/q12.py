test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(elections.take([0, 1, 2]).as_text(3))
          year | state    | south | democrat
          1932 | Alabama  | True  | 84.76%
          1932 | Arizona  | False | 67.03%
          1932 | Arkansas | True  | 86.27%
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
