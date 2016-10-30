test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> changes_by_state.num_rows
          50
          >>> int(max(changes_by_state.column(1)))
          17
          >>> int(min(changes_by_state.column(1)))
          -11
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
