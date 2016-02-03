test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> evens_only.num_rows
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(evens_only.column('Last Name'))
          ['Chen', 'Lau']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> evens_only.num_columns
          7
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
