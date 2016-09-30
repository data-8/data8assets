test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you forgot to have your function return something.
          >>> simulate_key_strike() is not None
          True
          >>> import string
          >>> all([simulate_key_strike() in string.ascii_lowercase for i in range(100)])
          True
          >>> # It looks like you didn't use all the letters of the alphabet, or you
          >>> # used too many.
          >>> import numpy as np
          >>> 26 >= len(np.unique([simulate_key_strike() for i in range(500)])) >= 20
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
