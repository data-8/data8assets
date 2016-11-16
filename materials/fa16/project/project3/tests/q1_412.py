test = {
  'name': 'Question 4.1.2',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.isclose(solo_accuracies.index_by('Feature').get('heart')[0][1], 0.62790697674418605)
          True
          >>> solo_accuracies.labels == ('Feature', 'Solo Accuracy')
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
