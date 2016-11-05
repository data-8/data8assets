test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you forgot to return something.
          >>> total_squared_error(0, 0) is not None
          True
          >>> # It looks like you took a square root, but
          >>> # we didn't want you to do that in this exercise.
          >>> not np.allclose(15.25**0.5, total_squared_error(0, 0))
          True
          >>> # Your calculation is incorrect in some way.
          >>> np.allclose(15.25, total_squared_error(0, 0))
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
