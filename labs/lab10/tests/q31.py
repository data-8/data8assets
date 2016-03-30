test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> c = make_best_knn_classifier(lyrics.take(range(20)), lyrics.take(range(20, 25)))
          >>> import collections
          >>> # make_best_knn_classifier should return a function.
          >>> isinstance(c, collections.Callable)
          True
          >>> # It looks like your classifier doesn't behave like the correct
          >>> # one does.
          >>> c(lyrics.drop(0).row(30)) == 'Hip-hop'
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
