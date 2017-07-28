test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your answer should be a number
          >>> type(mark_hurd_pay) != str
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Don't forget to give your answer in dollars, not millions of 
          >>> # Dollars! 
          >>> mark_hurd_pay != 5325
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Don't forget to give your answer in dollars, not millions of 
          >>> # Dollars! 
          >>> mark_hurd_pay == 53250000
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
