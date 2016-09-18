test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from datascience import *
          >>> type(with_dates) == tables.Table
          True
          >>> with_dates.num_columns
          3
          >>> "Date" in with_dates.labels
          True
          >>> all(with_dates.column("Raw text") == reuters.column("Raw text"))
          True
          >>> with_dates.column("Date").item(84)
          180
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
