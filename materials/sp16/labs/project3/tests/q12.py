test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure the columns are in the right order.
          >>> ak_mn.labels != ('Year', 'Minnesota', 'Alaska')
          True
          >>> ak_mn.labels
          ('Year', 'Alaska', 'Minnesota')
          >>> ak_mn.num_rows
          44
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
