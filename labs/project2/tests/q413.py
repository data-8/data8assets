test = {
  'name': 'Question 4.1.3',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.isclose(ablation_accuracies.index_by('Feature').get('heart')[0][1], 0.75813953488372088)
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
