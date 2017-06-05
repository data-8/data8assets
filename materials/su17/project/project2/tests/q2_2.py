test = {
  'name': 'Question 2.2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> changes_by_state.num_rows
          50
          >>> list(changes_by_state.row(0)) == ['Alabama', -6]
          True
          >>> list(changes_by_state.row(1)) == ['Alaska', -5]
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
