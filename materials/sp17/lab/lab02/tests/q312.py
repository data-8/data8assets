test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't load an image.  Hint:
          >>> # your code should start like this:
          >>> #   art = IPython.display.Image(...
          >>> import IPython.display
          >>> type(art) == IPython.core.display.Image
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you loaded the wrong image.
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
