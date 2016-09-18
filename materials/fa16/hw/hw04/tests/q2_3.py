test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from datascience import *
          >>> type(with_titles) == tables.Table
          True
          >>> with_titles.num_columns
          2
          >>> "Title" in with_titles.labels
          True
          >>> all(with_titles.column("Raw text") == reuters.column("Raw text"))
          True
          >>> with_titles.column("Title").item(4)
          'DEFENSE CONTRACTOR BOOSTS BIRD <BIRD> STAKE'
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
