test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(num_outcomes)
          50
          >>> import numpy as np
          >>> all(num_outcomes * .5**np.arange(1, 50+1) == 1.0)
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
