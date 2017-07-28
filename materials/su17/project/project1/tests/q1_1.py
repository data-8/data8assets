test = {
  'name': 'Question 1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Looks like you haven't started yet
          >>> type(b_pop) == type(...)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Check your column labels and spelling
          >>> b_pop.labels == ('time', 'population_total')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Times should range from 1970 through 2015
          >>> all(b_pop.sort("time").column("time") == np.arange(1970, 2016))
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
