test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = hashlib.md5(str(dem_year_california).encode())
          >>> x.digest() == b'\x11\x10\x8a=\xbf\xe4cl\xb4\x0b\x84\xb8\x03\xb2\xff\xf6'
          True
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
