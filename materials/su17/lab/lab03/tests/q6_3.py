test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sorted(farmers_markets_locations.labels)
          ['MarketName', 'State', 'city', 'x', 'y']
          >>> farmers_markets_locations.num_rows == 8546
          True
          >>> farmers_markets_locations.sort(0).take(range(3))
          MarketName                                       | city      | State    | y       | x
           Caledonia Farmers Market Association - Danville | Danville  | Vermont  | 44.411  | -72.1403
           Stearns Homestead Farmers' Market               | Parma     | Ohio     | 41.3751 | -81.7286
          100 Mile Market                                  | Kalamazoo | Michigan | 42.296  | -85.5749
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
