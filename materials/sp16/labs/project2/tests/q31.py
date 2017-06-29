test = {
  'name': 'Question 3.1',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.isclose(distance(a1, a2), 3.46410161513)
          True
          >>> np.isclose(distance(a2, a3), 6.16441400296)
          True
          >>> np.isclose(distance(a1, a3), 8.60232526704)
          True
          >>> np.isclose(distance(a1, a1), 0.0)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(distance_first_to_first, 0.21646718922539046)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': r"""
      import numpy as np
      a1 = np.array([1, 2, 3])
      a2 = np.array([3, 4, 5])
      a3 = np.array([9, 5, 4])
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
