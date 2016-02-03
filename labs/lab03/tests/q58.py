test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> correct_pets.num_columns
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(correct_pets.column('# Pets'))
          [1, 1, 1, 2, 3]
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
