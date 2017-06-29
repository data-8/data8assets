test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(pop_cleaned) == Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> pop_cleaned.labels
          ('year', 'population')
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> pop_cleaned.num_rows
          66
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> pop_cleaned.column("year").item(0)
          1950
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> pop_cleaned.column("population").item(0)
          2557628654
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
