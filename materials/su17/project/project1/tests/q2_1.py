test = {
  'name': 'Question 2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Please don't edit the last line.
          >>> latest.labels == ('geo', 'time', 'poverty_percent')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The result should have one row per country.
          >>> latest.num_rows
          145
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
