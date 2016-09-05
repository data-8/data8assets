test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't define a function named best_hands.
          >>> 'best_hands' in globals()
          True
          >>> one_game = Table().with_columns("Player", ["A"]*5, "Rank", [2, 2, 3, 4, 5], "Suit", ["♥︎", "♦︎", "♦︎", "♦︎", "♦︎"], "Game", [1]*5)
          >>> best_hands(one_game)
          Game | Biggest set in game
          1    | 2
          >>> two_games = Table().with_columns("Player", ["A"]*5 + ["B"]*10, "Rank", [2, 3, 4, 5, 6, 4, 4, 4, 5, 6, 4, 5, 6, 7, 8], "Suit", ["♥︎", "♦︎", "♥︎", "♦︎", "♦︎", "♣︎", "♦︎", "♠︎", "♠︎", "♠︎"] + ["♠︎"]*5, "Game", [1]*10 + [2]*5)
          >>> best_hands(two_games)
          Game | Biggest set in game
          1    | 3
          2    | 1
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
