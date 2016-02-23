test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(alameda_and_east_bay)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(alameda_and_east_bay[0]) == Region
          True
          >>> type(alameda_and_east_bay[1]) == Region
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
