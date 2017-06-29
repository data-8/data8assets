test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure you actually assign array_of_three_things to a NumPy array!
          >>> type(array_of_three_things) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(array_of_three_things)
          3
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
