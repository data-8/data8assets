test = {
  'name': 'Question 1.2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure the columns are in the right order.
          >>> ak_mn.labels != ('Year', 'Murder rate in Minnesota', 'Murder rate in Alaska')
          True
          >>> ak_mn.labels
          ('Year', 'Murder rate in Alaska', 'Murder rate in Minnesota')
          >>> ak_mn.num_rows
          44
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(ak_mn.sort('Year').take([3, 7, 11]))
          Year | Murder rate in Alaska | Murder rate in Minnesota
          1963 | 6.5                   | 1.2
          1967 | 9.6                   | 1.6
          1971 | 13.4                  | 2.4
          """,
          'hidden': True,
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
