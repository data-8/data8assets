test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your answer looks pretty far off -- maybe you're using the wrong formula?
          >>> round(also_roughly_e, 1)
          2.7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(also_roughly_e, 4)
          2.7183
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you didn't use n in your expression for
          >>> # also_roughly_e.
          >>> # Hint: It should start like this:
          >>> #   also_roughly_e = (1 + 1/n)...
          >>> round(1 / (also_roughly_e**(1/n) - 1), 2) == round(n, 2)
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
