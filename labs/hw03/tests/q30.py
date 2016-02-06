test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(dem_years.as_text())
          year | dem states
          1932 | 40
          1936 | 45
          1940 | 38
          1944 | 36
          1948 | 22
          1952 | 8
          1956 | 6
          1960 | 21
          1964 | 45
          1968 | 6
          1972 | 2
          1976 | 21
          1980 | 2
          1984 | 1
          1988 | 11
          1992 | 2
          1996 | 19
          2000 | 15
          2004 | 19
          2008 | 27
          2012 | 27
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import hashlib',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
