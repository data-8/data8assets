test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from datascience import *
          >>> type(students_by_city) == tables.Table
          True
          >>> students_by_city.num_columns
          2
          >>> students_by_city.num_rows
          52
          >>> students_by_city.sort('Number of full-time undergraduates', descending=True).take(range(5))
          City          | Number of full-time undergraduates
          San Francisco | 62772
          San Jose      | 35381
          Berkeley      | 30714
          Hayward       | 20610
          Stockton      | 20062
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
