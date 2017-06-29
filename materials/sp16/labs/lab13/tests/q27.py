test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> regression_lines_with_predictions.column(2).item(1) == regression_lines_with_predictions.column(1).item(1) + 5 * regression_lines_with_predictions.column(0).item(1)
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
