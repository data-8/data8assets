test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't define a function named winner.
          >>> 'winner' in globals()
          True
          >>> one_player = Table().with_columns("Player", ["A"]*5, "Rank", [2, 2, 3, 4, 5], "Suit", ["♥︎", "♦︎", "♦︎", "♦︎", "♦︎"])
          >>> winner(one_player)
          'A'
          >>> two_players = Table().with_columns("Player", ["A"]*5 + ["B"]*5, "Rank", [2, 3, 4, 5, 6, 4, 4, 4, 5, 6], "Suit", ["♥︎", "♦︎", "♥︎", "♦︎", "♦︎", "♣︎", "♦︎", "♠︎", "♠︎", "♠︎"])
          >>> winner(two_players)
          'B'
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
