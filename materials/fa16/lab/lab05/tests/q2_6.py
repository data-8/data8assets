test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure you're returning a single number
          >>> np.isscalar(tvd_from_eligible_population(make_array(.5, .5)))
          True
          >>> abs(tvd_from_eligible_population(make_array(.5, .5)) - 0.24) < .1
          True
          >>> abs(tvd_from_eligible_population(with_proportions.column("Proportion in panel")) - 0.18) < .1
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
