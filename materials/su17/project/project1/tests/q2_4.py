test = {
  'name': 'Question 2_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Check your column labels and spelling
          >>> poverty_map.labels == ('latitude', 'longitude', 'name', 'region', 'poverty_total')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Something is wrong with your region column.
          >>> list(np.sort(np.unique(poverty_map.column('region'))))
          ['africa', 'americas', 'asia', 'europe']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(poverty_map.sort('name').take(np.arange(10)).drop(4))
          latitude | longitude | name       | region
          41       | 20        | Albania    | europe
          28       | 3         | Algeria    | africa
          -12.5    | 18.5      | Angola     | africa
          -34      | -64       | Argentina  | americas
          40.25    | 45        | Armenia    | europe
          -25      | 135       | Australia  | asia
          47.3333  | 13.3333   | Austria    | europe
          40.5     | 47.5      | Azerbaijan | europe
          24       | 90        | Bangladesh | asia
          53       | 28        | Belarus    | europe
          """,
          'hidden': True,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(poverty_map.column(4)) == sum(recent.column(3))
          True
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
