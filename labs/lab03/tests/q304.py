test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You're off by 1.  Think about a smaller example, like 0 to 11.
          >>> index_of_last_element != 400
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You're off by 1.  Think about a smaller example, like 0 to 11.
          >>> index_of_last_element != 402
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> index_of_last_element
          401
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
