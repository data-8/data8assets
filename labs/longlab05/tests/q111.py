test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # observations should be an array of 14 randomly-generated
          >>> # numbers.
          >>> len(observations)
          14
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Each observation should be between 1 and N.
          >>> all(observations <= N) and all(observations >= 1)
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
