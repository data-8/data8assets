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
          >>> remaining_inventory
          box ID | fruit name | count
          53686  | kiwi       | 42
          57181  | strawberry | 22
          25274  | apple      | 20
          48800  | orange     | 0
          26187  | strawberry | 230
          57930  | grape      | 162
          52357  | strawberry | 0
          43566  | peach      | 23
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
