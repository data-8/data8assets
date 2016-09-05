test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> compensation_order.take(range(5))
          First Name | Last Name | Company        | Headquarters  | Total compensation ($) | Cash compensation ($) | Stock compensation ($) | Other compensation ($) | Change from previous year
          Mark       | Hurd      | Oracle         | Redwood City  | 5.325e+07              | 950000                | 5.227e+07              | 20000                  | 0
          Safra      | Catz      | Oracle         | Redwood City  | 5.324e+07              | 950000                | 5.227e+07              | 20000                  | 0
          Robert     | Iger      | Walt Disney    | Burbank       | 4.491e+07              | 2.489e+07             | 1.728e+07              | 2.74e+06               | -0.03
          Marissa    | Mayer     | Yahoo!         | Sunnyvale     | 3.598e+07              | 1e+06                 | 3.443e+07              | 550000                 | -0.15
          Marc       | Benioff   | salesforce.com | San Francisco | 3.336e+07              | 4.65e+06              | 2.726e+07              | 1.45e+06               | -0.16
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
