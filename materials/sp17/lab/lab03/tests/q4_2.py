test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(imdb_by_year) == tables.Table
          True
          >>> list(imdb_by_year.column('Title').take(range(3)))
          ['The Kid', 'The Gold Rush', 'The General']
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
