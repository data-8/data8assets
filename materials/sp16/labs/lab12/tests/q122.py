test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(max_deviation(couples, 'Gender', 'Relationship Rating'), 5) == 0.04550
          True
          >>> round(max_deviation(diffs, 'Marital Status', 'Relationship Rating ptp'), 5) == 0.05894
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
