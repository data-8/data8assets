test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Some of the true longevities are 1 year different from the
          >>> # ones you calculated earlier...
          >>> float(max(abs(true_longevity - longevity)))
          1.0
          >>> # ...but some are the same.
          >>> float(min(abs(true_longevity - longevity)))
          0.0
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
