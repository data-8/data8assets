test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> abs(np.mean([simulate_under_null() for _ in range(1000)]) - 10) <= .4
          True
          >>> # It looks like your simulation isn't random.
          >>> np.std([simulate_under_null() for _ in range(1000)]) > 0
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
