test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(cali) == Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> cali.num_rows
          21
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'from datascience import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
