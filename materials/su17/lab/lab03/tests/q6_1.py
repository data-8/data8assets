test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> farmers_markets.select(range(3)).take(range(3)).sort(0)
          FMID    | MarketName                                       | Website
          1011871 |  Stearns Homestead Farmers' Market               | http://Stearnshomestead.com
          1011878 | 100 Mile Market                                  | http://www.pfcmarkets.com
          1012063 |  Caledonia Farmers Market Association - Danville | https://sites.google.com/site/caledoniafarmersmarket/
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
