test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose([wait_below_3(1), wait_below_3(3), wait_above_3(3), wait_above_3(6)], [47.902151605742517, 60.603197182023813, 72.965413990538366, 89.281859197449506])
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
