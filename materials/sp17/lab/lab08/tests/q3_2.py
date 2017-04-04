test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure your column labels are correct.
          >>> faithful_predictions.labels == ('duration', 'wait', 'predicted wait')
          True
          >>> abs(1 - np.mean(faithful_predictions.column(2))/100) <= 0.35
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
