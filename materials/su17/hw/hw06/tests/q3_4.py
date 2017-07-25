test = {
  'name': 'Question 3_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0.4 <= lower_limit < upper_limit <= 0.7
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(lower_limit, 0.47506253911140456)
          True
          >>> np.isclose(upper_limit, 0.5749374608885954)
          True
          """,
          'hidden': True,
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
