test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> abs(5.7 - np.std([simulate_observations() for _ in range(5000)])) < .2
          True
          >>> abs(21.5 - np.mean([simulate_observations() for _ in range(5000)])) < .2
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
