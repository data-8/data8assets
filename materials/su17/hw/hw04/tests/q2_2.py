test = {
  'name': 'Question 2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> int(num_required_for_50_percent) == num_required_for_50_percent
          True
          >>> 20 < num_required_for_50_percent <= 100
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> abs(num_required_for_50_percent - 69) <= 11
          True
          """,
          'hidden': True,
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
