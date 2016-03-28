test = {
  'name': 'Question 4.1.1',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.isclose(accuracy_on(test_lyrics)(features_staff, 5), 0.7058823529411765)
          True
          >>> np.isclose(accuracy_on(test_lyrics)(features_staff, 1), 0.6099071207430341)
          True
          >>> np.isclose(accuracy_on(valid_lyrics)(features_staff, 1), 0.7255813953488373)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': r"""
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
