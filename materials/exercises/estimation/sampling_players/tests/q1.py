test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> full_data.num_rows
          492
          >>> full_data.select(sorted(full_data.labels)).sort(4).take(range(3))
          Age  | Assists | Blocks | Games | Name         | Points | Rebounds | Salary  | Steals | Team | Turnovers
          28   | 46      | 0      | 26    | A.J. Price   | 133    | 32       | 62552   | 7      | TOT  | 14
          30   | 261     | 15     | 82    | Aaron Brooks | 954    | 166      | 1145685 | 54     | CHI  | 157
          19   | 33      | 22     | 47    | Aaron Gordon | 243    | 169      | 3992040 | 21     | ORL  | 38
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
