test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from datascience import *
          >>> type(students_and_grants_by_state) == tables.Table
          True
          >>> students_and_grants_by_state.num_columns
          3
          >>> students_and_grants_by_state.num_rows
          59
          >>> students_and_grants_by_state.take(range(5))
          State (abbreviated) | Number of Pell grant recipients | Number of undergraduates
          AK                  | 8318                            | 31522
          AL                  | 118944                          | 269650
          AR                  | 75434                           | 164062
          AS                  | 914                             | 1795
          AZ                  | 304393                          | 648368
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
