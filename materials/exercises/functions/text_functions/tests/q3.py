test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you forgot to write "return" somewhere.
          >>> character_count("The quick(!) brown fox jumped over the lazy(?) dog.") is not None
          True
          >>> character_count("The quick(!) brown fox jumped over the lazy(?) dog.")
          40
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
