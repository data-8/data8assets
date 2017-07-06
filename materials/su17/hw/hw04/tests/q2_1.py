test = {
  'name': 'Question 2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 < chance_to_find_syringe < 0.5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> abs(chance_to_find_syringe - 0.182) < .06
          True
          """,
          'hidden': True,
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
