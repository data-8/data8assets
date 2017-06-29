test = {
  'name': 'Question 3.3.1',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> proportion_correct == r
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': r"""
      r = np.count_nonzero(test_guesses == test_lyrics.column('Genre')) / test_lyrics.num_rows
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
