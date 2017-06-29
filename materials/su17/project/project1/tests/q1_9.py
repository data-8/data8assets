test = {
  'name': 'Question 1_9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Please use a list of integers from 1 to 6
          >>> all(x in range(1, 7) for x in set(fertility_statements))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(fertility_statements)
          {1, 3, 4, 5, 6}
          """,
          'hidden': True,
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
