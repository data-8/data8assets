test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(coefficients)
          13
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.mean(np.abs(coefficients)) > 300
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
