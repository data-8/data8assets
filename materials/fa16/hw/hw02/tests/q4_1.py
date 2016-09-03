test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import re
          >>> all([bool(re.match('[HT]{4}', o)) for o in outcomes])
          True
          >>> len(outcomes)
          3
          >>> import numpy as np
          >>> len(np.unique(outcomes))
          3
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
