test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> income.labels
          ('ZIP', 'num returns', 'total income ($)', 'num farmers')
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> income.take([0, 1, 2])
          ZIP   | num returns | total income ($) | num farmers
          90001 | 20970       | 531,772          | 0
          90002 | 18960       | 467,128          | 0
          90003 | 26180       | 618,848          | 0
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
