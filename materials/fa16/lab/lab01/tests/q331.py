test = {
  'name': '3.3.1.',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Fill in the row
          >>> #   time = ...
          >>> # with something like:
          >>> #   time = 4.567
          >>> # (except with the right number).
          >>> time != ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Read the text above the question to see what
          >>> # time should be.
          >>> round(time, 5)
          1.2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Fill in the row
          >>> #   estimated_distance_m = ...
          >>> # with something like:
          >>> #   estimated_distance_m = 4.567
          >>> # (except with the right number).
          >>> estimated_distance_m != ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Note that the units are meters, but the text used
          >>> # centimeters.
          >>> estimated_distance_m != 113
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Read the text above the question to see what
          >>> # estimated_distance_m should be.
          >>> round(estimated_distance_m, 5)
          1.13
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
