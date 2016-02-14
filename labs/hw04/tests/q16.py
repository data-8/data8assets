test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(ahs_named) == Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 'SMSA name' in ahs_named.labels
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(ahs_named.column('SMSA name')) == {'Oakland', 'San Francisco', 'San Jose', 'Santa Rosa - Petaluma', 'Vallejo - Fairfield - Napa'}
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
