test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> your_classifier = make_best_knn_classifier(lyrics.take(range(20)), lyrics.take(range(20, 25)))
          >>> import collections
          >>> # make_best_knn_classifier should return a function.
          >>> isinstance(your_classifier, collections.Callable)
          True
          >>> # It looks like your function doesn't produce classifiers that
          >>> # behave as expected.
          >>> expected_classifier = make_knn_classifier(lyrics.take(range(20)), 1)
          >>> np.all(lyrics.drop(0).apply(your_classifier) == lyrics.drop(0).apply(expected_classifier))
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
