test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(my_flower) == list
          True
          >>> type(my_flower[0]) == int
          True
          >>> type(my_flower[1]) == str and my_flower[1] != ''
          True
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
