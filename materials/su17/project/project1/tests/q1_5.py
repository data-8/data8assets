test = {
  'name': 'Question 1_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Check your column labels and spelling
          >>> fertility_over_time('usa', 2010).labels == ('Year', 'Children per woman')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Check that you use the start year to determine the data range.
          >>> all(fertility_over_time('usa', 2010).column('Year') == np.arange(2010, 2016))
          True
          >>> all(fertility_over_time('usa', 2005).column('Year') == np.arange(2005, 2016))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(fertility_over_time('bgd', 2009))
          Year | Children per woman
          2009 | 2.32
          2010 | 2.28
          2011 | 2.24
          2012 | 2.21
          2013 | 2.18
          2014 | 2.15
          2015 | 2.12
          """,
          'hidden': True,
          'locked': False
        },
        {
          'code': r"""
          >>> print(fertility_over_time('usa', 2010))
          Year | Children per woman
          2010 | 1.93
          2011 | 1.9
          2012 | 1.9
          2013 | 1.98
          2014 | 1.97
          2015 | 1.97
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
