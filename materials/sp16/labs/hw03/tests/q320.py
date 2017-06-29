test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> overall_dem_vote_per_state.num_columns
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> together.num_columns
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> easy_inspection.column(2).item(15)
          413
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
