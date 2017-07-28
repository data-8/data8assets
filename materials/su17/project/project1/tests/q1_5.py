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
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
