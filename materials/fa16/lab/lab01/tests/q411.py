test = {
  'name': '4.1.1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Fill in the line
          >>> #   num_avenues_away = ...
          >>> # in the cell above. 
          >>> num_avenues_away != ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Remember to compute the absolute value of 7-10.  Traveling 
          >>> # "-3 blocks" doesn't really make sense!
          >>> num_avenues_away != -3
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> num_avenues_away
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> manhattan_distance
          1462
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
