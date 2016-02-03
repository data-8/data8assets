test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [

        {
          'code': r"""
          >>> joke
          19
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
