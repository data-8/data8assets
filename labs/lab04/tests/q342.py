test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> depends_on("Chocolate Bar")
          'Chocolate Bar is a String!'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> depends_on(7)
          49
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> depends_on(False)
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
