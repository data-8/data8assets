test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you forgot to write "return" somewhere.
          >>> chapter_number("XIV. Chapter Fourteen\nIt was the most mediocre of times...") is not None
          True
          >>> chapter_number("XIV. Chapter Fourteen\nIt was the most mediocre of times...")
          'XIV'
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
