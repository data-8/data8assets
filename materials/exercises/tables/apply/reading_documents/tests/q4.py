test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you forgot to have get_date return something.
          >>> get_date(reuters.column("Raw text").item(42)) is not None
          True
          >>> get_date(reuters.column("Raw text").item(42))
          170
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
