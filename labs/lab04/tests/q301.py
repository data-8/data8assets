test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> is_greater(5, 10) == False
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_greater('no', 'hi')
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