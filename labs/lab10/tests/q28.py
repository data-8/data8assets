test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Think about classifying a song in the training set.  Since it's
          >>> # in the training set, when the 1-NN classifier looks for its
          >>> # single nearest neighbor in the training set, the song is its
          >>> # own nearest neighbor!  So it gets classified with its own
          >>> # genre, which is of course correct.
          >>> q28_accuracy == 1.0
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
