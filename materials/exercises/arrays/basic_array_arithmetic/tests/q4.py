test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you multiplied -32 by 5/9, but not the array
          >>> # of temperatures.  Try using parentheses.
          >>> round(sum(celsius_max_temperatures)) != 3229921.0
          True
          >>> # It looks like you multipied and subtracted in the wrong
          >>> # order.
          >>> round(sum(celsius_max_temperatures)) != 356376.0
          True
          >>> round(sum(celsius_max_temperatures))
          1280821.0
          >>> len(celsius_max_temperatures)
          65000
          >>> celsius_max_temperatures.item(2003)
          20.0
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
