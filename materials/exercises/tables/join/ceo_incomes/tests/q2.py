test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> companies_per_sector.sort("count").take(range(5))
          Sector            | count
          Consumer Durables | 1
          Energy            | 2
          Public Utilities  | 2
          Basic Industries  | 4
          Finance           | 4
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
