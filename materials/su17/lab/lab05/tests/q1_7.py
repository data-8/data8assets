test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> (result == 'Wow!') or (result == 'Meh.') or (result == 'Okay!')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ten_nachos = make_array('neither', 'cheese', 'both', 'both', 'cheese', 'salsa', 'both', 'neither', 'cheese', 'both')
          >>> ten_nachos_reactions = Table().with_column('Nachos', ten_nachos)
          >>> ten_nachos_reactions = ten_nachos_reactions.with_column('Reactions', ten_nachos_reactions.apply(nacho_reaction, 'Nachos'))
          >>> both_or_neither(ten_nachos_reactions)
          'Wow!'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> seven_nachos = make_array('neither', 'cheese', 'both', 'both', 'neither', 'both', 'neither')
          >>> seven_nachos_reactions = Table().with_column('Nachos', seven_nachos)
          >>> seven_nachos_reactions = seven_nachos_reactions.with_column('Reactions', seven_nachos_reactions.apply(nacho_reaction, 'Nachos'))
          >>> both_or_neither(seven_nachos_reactions)
          'Okay!'
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
