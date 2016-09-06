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
          >>> imdb_by_year.column('Title').take(range(3))
          array(['The Kid (1921)', 'The Gold Rush (1925)', 'The General (1926)'], 
                dtype='<U75')
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
