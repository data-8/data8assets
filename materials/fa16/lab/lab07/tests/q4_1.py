test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 12 - zero_minute_predicted_waiting_time*1.4/4 <= 0.35
          True          
          >>> 2 - two_point_five_minute_predicted_waiting_time/35 <= 0.4
          True
          >>> (26 - hour_predicted_waiting_time/30)/10 <= 0.43
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
