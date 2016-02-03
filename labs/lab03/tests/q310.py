test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(small_square_roots) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(small_square_roots)
          21
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> approx_equals(small_square_roots, np.sqrt(np.arange(0, 20+1, 1)))
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': 'def approx_equals(a, b): return np.linalg.norm(a - b) < 1e-6',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
