test = {
  'name': 'Question 3.1.1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(my_20_features)
          20
          >>> np.all([f in test_lyrics.labels for f in my_20_features])
          True
          >>> # It looks like there are some songs in the training set that
          >>> # don't have any of your chosen words.  That will make your
          >>> # classifier perform very poorly in some cases.  Try choosing
          >>> # at least 1 common word.
          >>> train_f = train_lyrics.select(my_20_features)
          >>> np.count_nonzero(train_f.apply(lambda r: np.sum(np.abs(np.array(r))) == 0)) < 150
          True
          >>> # It looks like there are some songs in the test set that
          >>> # don't have any of your chosen words.  That will make your
          >>> # classifier perform very poorly in some cases.  Try choosing
          >>> # at least 1 common word.
          >>> test_f = test_lyrics.select(my_20_features)
          >>> np.count_nonzero(train_f.apply(lambda r: np.sum(np.abs(np.array(r))) == 0)) < 100
          True
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
