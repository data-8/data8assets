test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 2 < number_wow_reactions < 6
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Incorrect value for number_wow_reactions
          >>> number_wow_reactions == 4
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
