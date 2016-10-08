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
          >>> students_and_grants_by_state.select(sorted(students_and_grants_by_state.labels)).take(range(5))
          Number of Pell grant recipients | Number of undergraduates | State (abbreviated)
          8318                            | 31522                    | AK
          118944                          | 269650                   | AL
          75434                           | 164062                   | AR
          914                             | 1795                     | AS
          304393                          | 648368                   | AZ
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
