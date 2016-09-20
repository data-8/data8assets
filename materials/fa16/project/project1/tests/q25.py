test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you're not accounting for the size of each
          >>> # ZIP code.  What would your code do if there were only 1
          >>> # person in 94576?
          >>> average_income != 61598
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> average_income
          52773
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
