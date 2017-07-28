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
          >>> print(really_highly_rated.sort(0).take([3, 17]))
          Votes  | Rating | Title           | Year | Decade
          358305 | 8.6    | La vita è bella | 1997 | 1990
          895411 | 8.6    | Se7en           | 1995 | 1990
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
