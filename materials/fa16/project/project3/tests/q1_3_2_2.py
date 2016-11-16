test = {
  'name': 'Question 3.2.2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> grandpa_genre == grandpa_expected_genre
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': r"""
      from collections import Counter
      g = train_lyrics.column('Genre')
      r = np.where(test_lyrics['Title'] == "Grandpa Got Runned Over By A John Deere")[0][0]
      t = test_20.row(r)
      grandpa_expected_genre = Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:9])).most_common(1)[0][0]
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
