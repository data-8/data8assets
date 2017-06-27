test = {
  'name': 'Question 3_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you might have the right answer, but you need to
          >>> # relabel one of the rows of the table.
          >>> "count" not in complaints_per_company.labels
          True
          >>> complaints_per_company.select(sorted(complaints_per_company.labels)).sort(0).take(range(4))
          company                   | number of complaints
          1st Preference Mortgage   | 2
          21st Mortgage Corporation | 7
          2288984 Ontario Inc.      | 3
          360 Mortgage              | 1
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
