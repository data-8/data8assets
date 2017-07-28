test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(some_functions)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The first thing in your array may not be a function
          >>> callable(some_functions.item(0))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The second thing in your array may not be a function
          >>> callable(some_functions.item(1))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The third thing in your array may not be a function
          >>> callable(some_functions.item(1))
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
