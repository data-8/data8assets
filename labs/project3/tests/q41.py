test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0.1 <= sign_test(death_penalty_murder_rates, 1960, 1962) <= 0.2
          Increases minus decreases 1960 to 1962 : -9
          True
          >>> 0.04 <= sign_test(murder_rates, 1960, 1962) <= 0.1
          Increases minus decreases 1960 to 1962 : -13
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
