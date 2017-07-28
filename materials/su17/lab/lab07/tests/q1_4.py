test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> # It looks like you forgot to return something.
          >>> mean_based_estimator(np.array([1, 2, 3])) is not None
          True
          >>> # It looks like your function doesn't compute the
          >>> # right estimate.  For consistency in the rest of the
          >>> # lab, it's best if you use the twice-the-mean estimate,
          >>> # even if you prefer some other estimate.
          >>> int(np.round(mean_based_estimator(np.array([1, 2, 3]))))
          4
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
