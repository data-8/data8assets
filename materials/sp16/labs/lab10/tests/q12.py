test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you're computing the *number* of right answers
          >>> # instead of the proportion.
          >>> proportion_right_answers != 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> proportion_right_answers
          0.4
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
