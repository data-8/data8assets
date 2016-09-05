test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from datascience import *
          >>> type(sfba_cities) == tables.Table
          True
          >>> sfba_cities.num_columns
          2
          >>> sfba_cities.num_rows
          53
          >>> sfba_cities.sort('Number of schools', descending=True).take(range(5))
          City          | Number of schools
          San Francisco | 23
          Oakland       | 14
          San Jose      | 12
          Berkeley      | 12
          Stockton      | 9
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
