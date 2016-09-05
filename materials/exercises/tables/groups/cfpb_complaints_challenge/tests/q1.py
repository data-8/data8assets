test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> many_products_companies.with_column('products with many complaints', many_products_companies.apply(sorted, 1)).sort(0)
          company               | products with many complaints
          Bank of America       | ['Bank account or service', 'Credit card', 'Mortgage']
          Citibank              | ['Bank account or service', 'Credit card']
          JPMorgan Chase & Co.  | ['Bank account or service', 'Credit card', 'Mortgage']
          Wells Fargo & Company | ['Bank account or service', 'Mortgage']
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
