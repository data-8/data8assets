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
        },
        {
          'code': r"""
          >>> list(region_counts.sort("count").column("count"))
          [5, 7, 8, 10, 10, 10]
          >>> list(region_counts.sort("count").column("region"))
          ['south_asia', 'middle_east_north_africa', 'america', 'east_asia_pacific', 'europe_central_asia', 'sub_saharan_africa']
          """,
          'hidden': True,
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
