test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sum(faithful_standard.column(0)) == 1.4011014570769476e-13
          True
          >>> int(round(duration_std))
          1
          >>> int(round(wait_std))
          14
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
