test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from datascience import tables
          >>> type(by_company_and_product) == tables.Table
          True
          >>> by_company_and_product.num_rows
          1582
          >>> by_company_and_product.take(range(5))
          company                                | product          | count
          Equifax                                | Credit reporting | 1432
          Experian                               | Credit reporting | 1236
          TransUnion Intermediate Holdings, Inc. | Credit reporting | 1026
          Wells Fargo & Company                  | Mortgage         | 463
          Ocwen                                  | Mortgage         | 318
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
