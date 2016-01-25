test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(interesting_numbers)
          numpy.ndarray
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(interesting_numbers)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import math
          >>> import numpy as np
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
