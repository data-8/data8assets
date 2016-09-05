test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your table doesn't have all 3 columns that are
          >>> # in the inventory table.
          >>> remaining_inventory.num_columns
          3
          >>> # It looks like you forgot to subtract off the sales.
          >>> remaining_inventory.column("count").item(0) != 45
          True
          >>> remaining_inventory.sort(0)
          box ID | fruit name | count
          25274  | apple      | 20
          26187  | strawberry | 230
          43566  | peach      | 23
          48800  | orange     | 0
          52357  | strawberry | 0
          53686  | kiwi       | 42
          57181  | strawberry | 22
          57930  | grape      | 162
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
