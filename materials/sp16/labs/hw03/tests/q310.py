test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = hashlib.md5(dem_state.encode())
          >>> x == b'\xac\'\x13\xab\xe8m\x88\xf03&\x15\x7f"\xa5\x08i'
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': 'import hashlib',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}