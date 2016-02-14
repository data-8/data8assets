test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(ahs_poverty) == Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ahs_poverty.num_rows
          1014
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # poverty should be a column of boolean values.
          >>> type(ahs_poverty.column("poverty").item(0)) == bool
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You didn't calculate poverty in the way we expected.
          >>> ahs_poverty.column("poverty").item(0)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You didn't calculate poverty in the way we expected.
          >>> np.count_nonzero(ahs_poverty.column("poverty"))
          164
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
