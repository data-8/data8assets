test = {
  'name': 'Question 3_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you might have the right answer, but you need to
          >>> # relabel one of the rows of the table.
          >>> "count" not in complaints_per_product.labels
          True
          >>> complaints_per_product.select(sorted(complaints_per_product.labels)).sort(0).take(range(4))
          number of complaints | product
          16                   | Other financial service
          110                  | Prepaid card
          119                  | Payday loan
          142                  | Money transfers
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
