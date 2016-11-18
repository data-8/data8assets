test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sorted(train_two_features.labels)
          ['Frame 1 x', 'Frame 1 y', 'Movement type']
          >>> train_two_features.num_rows == train_movements.num_rows
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
