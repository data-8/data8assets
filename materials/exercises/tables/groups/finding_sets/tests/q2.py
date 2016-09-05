test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't define a function named biggest_sets.
          >>> 'biggest_sets' in globals()
          True
          >>> one_player = Table().with_columns("Player", ["A"]*5, "Rank", [2, 2, 3, 4, 5], "Suit", ["♥︎", "♦︎", "♦︎", "♦︎", "♦︎"])
          >>> biggest_sets(one_player)
          Player | Biggest set
          A      | 2
          >>> two_players = Table().with_columns("Player", ["A"]*5 + ["B"]*5, "Rank", [2, 3, 4, 5, 6, 4, 4, 4, 5, 6], "Suit", ["♥︎", "♦︎", "♥︎", "♦︎", "♦︎", "♣︎", "♦︎", "♠︎", "♠︎", "♠︎"])
          >>> biggest_sets(two_players)
          Player | Biggest set
          A      | 1
          B      | 3
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
