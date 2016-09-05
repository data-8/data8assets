test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> alphabetical_order.take(range(5))
          First Name | Last Name | Company         | Headquarters  | Total compensation ($) | Cash compensation ($) | Stock compensation ($) | Other compensation ($) | Change from previous year | Rank
          Laura      | Alber     | Williams-Sonoma | San Francisco | 1.4e+07                | 3.97e+06              | 1e+07                  | 20000                  | -0.05                     | 29
          Martin     | Anstice   | Lam Research    | Fremont       | 1.116e+07              | 4.75e+06              | 6.41e+06               | 10000                  | -0.26                     | 39
          Robert     | Antin     | VCA             | Los Angeles   | 8.23e+06               | 3.57e+06              | 4.3e+06                | 370000                 | 0.19                      | 65
          Carl       | Bass      | Autodesk        | San Rafael    | 1.218e+07              | 2.48e+06              | 9.62e+06               | 80000                  | 0.1                       | 33
          Dan        | Batrack   | Tetra Tech      | Pasadena      | 5.42e+06               | 1.95e+06              | 3.43e+06               | 40000                  | 0.2                       | 82
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
