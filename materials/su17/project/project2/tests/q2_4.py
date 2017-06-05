test = {
  'name': 'Question 2.4',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # There are several two-year changes for each state.
          >>> num_changes != 50
          True
          >>> # The entire data set contains many states, not just 1.
          >>> not(42 <= num_changes <= 44)
          True
          >>> 2000 <= num_changes <= 2200
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
