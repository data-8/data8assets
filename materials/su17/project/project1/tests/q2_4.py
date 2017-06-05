test = {
  'name': 'Question 2_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Check your column labels and spelling
          >>> poverty_map.labels == ('latitude', 'longitude', 'name', 'region', 'poverty_total')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Something is wrong with your region column.
          >>> list(np.sort(np.unique(poverty_map.column('region'))))
          ['africa', 'americas', 'asia', 'europe']
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
