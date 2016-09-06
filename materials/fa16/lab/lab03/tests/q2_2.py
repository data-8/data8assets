test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(imdb) == tables.Table
          True
          >>> imdb.num_rows == 250
          True
          >>> imdb.select('Votes', 'Rating', 'Title', 'Year', 'Decade').sort(0).take(range(5))
          Votes | Rating | Title                              | Year | Decade
          26012 | 8      | Kumonosu-jô (1957)                 | 1957 | 1950
          28012 | 8      | Le samouraï (1967)                 | 1967 | 1960
          31003 | 8.1    | Le salaire de la peur (1953)       | 1953 | 1950
          32385 | 8      | La battaglia di Algeri (1966)      | 1966 | 1960
          35983 | 8.1    | The Best Years of Our Lives (1946) | 1946 | 1940
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
