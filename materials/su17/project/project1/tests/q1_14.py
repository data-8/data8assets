test = {
  'name': 'Question 1_14',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Please use a list of integers from 1 to 5
          >>> all(x in range(1, 6) for x in set(scatter_statements))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(scatter_statements)
          {1, 3, 4}
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
