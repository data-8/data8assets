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
          >>> float(round(np.mean(coefficients) / 1500) * 1500)
          1500.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> float(round(np.std(coefficients) / 25000) * 25000)
          25000.0
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
