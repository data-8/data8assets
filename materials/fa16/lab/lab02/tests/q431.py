test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you're not making an array.  You shouldn't need to
          >>> # use .item anywhere in your solution.
          >>> import numpy as np
          >>> type(population_magnitudes) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You made an array, but it doesn't have the right numbers in it.
          >>> import numpy as np
          >>> sum(abs(population_magnitudes - np.log10(population))) < 1e-6
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
