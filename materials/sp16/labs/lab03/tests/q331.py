test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(treatments_successful) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(treatments_successful == np.array([True, True, False, False, False]))
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
