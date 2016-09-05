test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> hand_of_4.num_rows
          4
          >>> sorted(hand_of_4.labels)
          ['Rank', 'Suit']
          >>> hand_of_4.group("Suit").sort("Suit")
          Suit | count
          ♠︎   | 1
          ♣︎   | 1
          ♥︎   | 1
          ♦︎   | 1
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
