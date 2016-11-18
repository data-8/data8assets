test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sorted(with_colors.labels)
          ['Color', 'Frame 1 x', 'Frame 1 y', 'Movement type']
          >>> with_colors.num_rows == train_movements.num_rows
          True
          >>> with_colors.sort("Frame 1 x").take(np.arange(5)).column("Color")
          array(['gold', 'gold', 'blue', 'blue', 'gold'], 
                dtype='<U4')
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
