test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> between_1990_and_2012.num_rows
          6
          >>> 
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> demVotes.item(3)
          53.45
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
           >>> x = hashlib.md5(str(difference).encode())
           >>> x.digest() == b'\x18\xef\xb2\x87D\xe8\xfeL\xcd\xe5\xd3V\xdaP\xa8o'
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