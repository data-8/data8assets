test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(really_highly_rated) == tables.Table
          True
          >>> really_highly_rated.num_rows == 29
          True
          >>> really_highly_rated.sort(0).take(range(10))
          Votes  | Rating | Title                                  | Year | Decade
          192206 | 8.6    | C'era una volta il West (1968)         | 1968 | 1960
          206216 | 8.7    | Shichinin no samurai (1954)            | 1954 | 1950
          242353 | 8.6    | It's a Wonderful Life (1946)           | 1946 | 1940
          358305 | 8.6    | La vita è bella (1997)                 | 1997 | 1990
          384187 | 8.9    | 12 Angry Men (1957)                    | 1957 | 1950
          447875 | 8.9    | Il buono, il brutto, il cattivo (1966) | 1966 | 1960
          476501 | 8.6    | Cidade de Deus (2002)                  | 2002 | 2000
          606395 | 8.7    | One Flew Over the Cuckoo's Nest (1975) | 1975 | 1970
          635139 | 8.6    | Léon (1994)                            | 1994 | 1990
          644556 | 8.7    | Goodfellas (1990)                      | 1990 | 1990
          
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
