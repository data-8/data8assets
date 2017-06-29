test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> state_spread.labels
          ('state', 'democrat spread')
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.round(sum(state_spread.column(1)), 2) == 19.33
          True
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
