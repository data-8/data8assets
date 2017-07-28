test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose([predict_wait(x) for x in [1.5, 2.5, 3.5, 4.5]], [51.077412999812836, 57.427935787953487, 75.684821525023551, 81.123636593993922])
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
