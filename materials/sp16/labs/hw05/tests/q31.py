test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your function doesn't return anything.
          >>> simulate_observations() is not None
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Your function doesn't return an array.
          >>> isinstance(simulate_observations(), np.ndarray)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Your function doesn't return an array of 14 things.
          >>> len(simulate_observations()) == 14
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You probably aren't using the right random process.
          >>> max([max(simulate_observations()) for i in range(200)]) == 120
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You probably aren't using the right random process.
          >>> min([min(simulate_observations()) for i in range(200)]) == 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You probably aren't using the right random process.
          >>> 57 <= np.average([np.average(simulate_observations()) for i in range(200)]) <= 64
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Your function should generate fresh random observations
          >>> # each time it's called.
          >>> not all(simulate_observations() == simulate_observations())
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
