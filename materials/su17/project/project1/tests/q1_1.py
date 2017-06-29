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
        },
        {
          'code': r"""
          >>> # See if you selected the right three-letter code!
          >>> b_pop.sort("time", descending=True).column("population_total").item(0)
          160995642
          >>> b_pop.sort("time").column("population_total").item(0)
          65048701
          """,
          'hidden': True,
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
