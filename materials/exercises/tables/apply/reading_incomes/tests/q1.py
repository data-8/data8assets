test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> raw_compensation.select("Rank", "Name", "Company (Headquarters)", "Total Pay").take(range(5))
          Rank | Name             | Company (Headquarters)         | Total Pay
          1    | Mark V. Hurd*    | Oracle (Redwood City)          | $53.25
          2    | Safra A. Catz*   | Oracle (Redwood City)          | $53.24
          3    | Robert A. Iger   | Walt Disney (Burbank)          | $44.91
          4    | Marissa A. Mayer | Yahoo! (Sunnyvale)             | $35.98
          5    | Marc Benioff     | salesforce.com (San Francisco) | $33.36
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
