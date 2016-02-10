test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> is_strictly_increasing(np.array([1,2,2]))
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_strictly_increasing(np.array([1, 3, 5]))
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import numpy as np',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
