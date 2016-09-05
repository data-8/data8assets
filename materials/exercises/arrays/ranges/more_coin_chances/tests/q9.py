test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(new_average_winnings)
          50
          >>> # It looks like your calculation isn't right.
          >>> import numpy as np
          >>> round(np.mean(new_average_winnings) - .2, 2)
          0.0
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
