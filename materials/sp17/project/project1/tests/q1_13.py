test = {
  'name': 'Question 1_13',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Check your column labels and spelling
          >>> region_counts.labels == ('region', 'count')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Counts must sum to 50
          >>> sum(region_counts.column('count')) == 50
          True
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
