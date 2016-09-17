test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> num_markets_in_california
          759
          >>> # It looks like you computed the proportion of all markets that
          >>> # are in Wisconsin and selling cheese.  Instead, look just at
          >>> # the markets that are in Wisconsin, and compute the proportion
          >>> # of those that sell cheese.
          >>> round(proportion_markets_selling_cheese_in_wisconsin, 3) != 0.012
          True
          >>> round(proportion_markets_selling_cheese_in_wisconsin, 2) == 0.34
          True
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
