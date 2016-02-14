test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(ahs_cleaned) == Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(ahs_cleaned.labels)
          310
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ahs_cleaned.num_rows
          1281
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ahs_cleaned.column("SMSA").item(0)
          7500
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
