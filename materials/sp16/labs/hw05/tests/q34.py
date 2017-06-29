test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(mean_based_estimator(np.array([1,2,3,4,10,50])), 5) == 23.33333
          True
          """,
          'hidden': False,
          'locked': False
        },

      ],
      'scored': True,
      'setup': 'import numpy as np',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}