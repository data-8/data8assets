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
        },
        {
          'code': r"""
          >>> int(max(changes_by_state.column(1)))
          17
          >>> int(min(changes_by_state.column(1)))
          -11
          >>> int(sum(changes_by_state.column(1)))
          45
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
