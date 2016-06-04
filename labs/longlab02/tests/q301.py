test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import IPython.display
          >>> type(art) == IPython.core.display.Image
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 'The_Death_of_Socrates' in art.url
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}