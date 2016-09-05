test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(average_winnings)
          50
          >>> import numpy as np
          >>> np.count_nonzero(average_winnings > 0)
          3
          >>> average_winnings.item(3)
          -0.375
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
