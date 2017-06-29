test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(intervals.labels) == 4
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(intervals.column(2) - intervals.column(1) == intervals.column(3))
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
