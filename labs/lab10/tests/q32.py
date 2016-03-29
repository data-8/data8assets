test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import collections
          >>> # Your classifier should be a function.
          >>> isinstance(best_knn_classifier, collections.Callable)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like your classifier doesn't behave like the correct
          >>> # one does.
          >>> c = make_best_knn_classifier(lyrics.take(range(80)), lyrics.take(range(80, 90)))
          >>> np.all(lyrics.drop(0).apply(c) == lyrics.drop(0).apply(best_knn_classifier))
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
