test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(list_of_lists) == list
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(list_of_lists)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list_of_lists == [['Hello', 'world', '!'], [True, False]]
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
