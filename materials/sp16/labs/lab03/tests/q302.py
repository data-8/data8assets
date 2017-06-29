test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # The argument to np.array was a single value, which
          >>> # happened to be a list that had 3 elements in it.
          >>> number_of_arguments != 3
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> number_of_arguments
          1
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
