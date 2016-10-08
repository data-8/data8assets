test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from datascience import *
          >>> type(pell_proportions) == tables.Table
          True
          >>> pell_proportions.num_columns
          2
          >>> pell_proportions.num_rows
          59
          >>> pell_proportions.select("State (abbreviated)", "Pell proportion").take(range(5))
          State (abbreviated) | Pell proportion
          AK                  | 0.263879
          AL                  | 0.441105
          AR                  | 0.45979
          AS                  | 0.509192
          AZ                  | 0.469476
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
