test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing the slope
          >>> abs(fit_line(example_table)[0] - 2) < .5
          True
          >>> # Testing the intercept
          >>> abs(fit_line(example_table)[1] - 1) < .5
          True
          >>> # Testing the slope
          >>> abs(fit_line(close_novas)[0] - 14094) < 5 
          True
          >>> # Testing the intercept
          >>> abs(fit_line(close_novas)[1] - 2) < .5
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
