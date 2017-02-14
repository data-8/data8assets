test = {
  'name': '4.2.1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Read the text above the question to see what
          >>> # estimated_distance_m should be.
          >>> round(estimated_distance_m, 5)
          1.13
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Compute predicted_distance_m using the formula in the text
          >>> # above.  Hint: it should start with something like this:
          >>> #   predicted_distance_m = (1/2) * gravity_constant ...
          >>> round(predicted_distance_m, 5)
          1.17022
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(difference, 5)
          0.04022
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
