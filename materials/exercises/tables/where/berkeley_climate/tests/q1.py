test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't make a table, or you didn't name
          >>> # it temperatures.
          >>> from datascience import *
          >>> type(temperatures) == tables.Table
          True
          >>> # It looks like you loaded the wrong table, or you changed.
          >>> # the table in some way.
          >>> temperatures.num_rows
          4998
          >>> temperatures.num_columns
          6
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
