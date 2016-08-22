test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(interesting_numbers) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(interesting_numbers)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(interesting_numbers == np.array([0, 1, -1, math.pi, math.e]))
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
