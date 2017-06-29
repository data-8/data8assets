test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure you actually set empty_list to a list!
          >>> type(empty_list) == list
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(empty_list)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure you actually set singleton_list to a list!
          >>> type(singleton_list) == list
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(singleton_list)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure you actually set list_of_five_things to a list!
          >>> type(list_of_five_things) == list
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(list_of_five_things)
          5
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
