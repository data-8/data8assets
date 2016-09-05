test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you haven't defined a function named word_count.
          >>> 'word_count' in globals()
          True
          >>> # It looks like you haven't defined a function named word_count.
          >>> callable(word_count)
          True
          >>> # It looks like you forgot to write "return" somewhere.
          >>> word_count("The quick brown fox") is not None
          True
          >>> word_count("The quick brown fox")
          4
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
