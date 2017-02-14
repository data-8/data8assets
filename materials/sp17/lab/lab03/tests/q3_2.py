test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(seven_flowers) == Table
          True
          >>> seven_flowers.num_rows
          7
          >>> seven_flowers.take([0, 1, 2, 4, 5, 6])
          Number of petals | Name
          8                | lotus
          34               | sunflower
          5                | rose
          10               | lavender
          3                | birds of paradise
          6                | tulip
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
