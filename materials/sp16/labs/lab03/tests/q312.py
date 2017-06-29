test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(pi_digits) ==  np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(pi_digits == np.array([3,  1,  4,  1,  5,  9,  2,  6,  5,  3,  5,  8]))
          True
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
