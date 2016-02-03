test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(growth_rates) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> approx_equals(growth_rates, wealth_ratios ** (1 / observation_intervals) - 1)
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
