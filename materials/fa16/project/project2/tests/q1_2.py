test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure the columns are in the right order.
          >>> ak_mn.labels != ('Year', 'Murder rate in Minnesota', 'Murder rate in Alaska')
          True
          >>> ak_mn.labels
          ('Year', 'Murder rate in Alaska', 'Murder rate in Minnesota')
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
