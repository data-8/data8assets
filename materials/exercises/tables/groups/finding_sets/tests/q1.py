test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't define a function named biggest_set.
          >>> 'biggest_set' in globals()
          True
          >>> biggest_set(deck.take(range(0, 10, 2)))
          2
          >>> biggest_set(deck.take(range(1, 6, 1)))
          3
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
