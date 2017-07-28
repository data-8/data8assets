test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> berkeley_markets.sort(0)
          MarketName                        | city     | State      | y       | x
          Downtown Berkeley Farmers' Market | Berkeley | California | 37.8697 | -122.273
          North Berkeley Farmers' Market    | Berkeley | California | 37.8802 | -122.269
          South Berkeley Farmers' Market    | Berkeley | California | 37.8478 | -122.272
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
