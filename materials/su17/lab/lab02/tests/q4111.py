test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(multiples_of_99) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(multiples_of_99)
          102
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(multiples_of_99 == np.arange(0, 9999+99, 99))
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
