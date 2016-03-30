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
