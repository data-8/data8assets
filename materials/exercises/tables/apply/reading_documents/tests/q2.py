test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you forgot to have get_title return something.
          >>> get_title(reuters.column("Raw text").item(1)) is not None
          True
          >>> get_title(reuters.column("Raw text").item(1))
          'DE LAURENTIIS COMPANIES SEE LOSS ON FILM'
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
