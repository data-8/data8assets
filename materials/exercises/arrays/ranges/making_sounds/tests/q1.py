test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like frame_times isn't an array.
          >>> import numpy as np
          >>> type(frame_times) == np.ndarray
          True
          >>> # Each frame should be 1/44100 seconds apart.
          >>> all(abs(np.diff(frame_times) - 1/44100) < 1e-10)
          True
          >>> len(frame_times) == 132300
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
