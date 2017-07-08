test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure your estimator is subtracting a reasonable value from the mean observation
          >>> ok_test_array = make_array(1, 2, 3, 4, 5, 6, 7)
          >>> abs(11 - (np.mean(ok_test_array) - mean_based_estimator(ok_test_array))) < 4
          True
          >>> ok_test_array = make_array(5, 4, 3, 6, 7, 1, 4, 12, 8)
          >>> abs(11 - (np.mean(ok_test_array) - mean_based_estimator(ok_test_array))) < 4
          True
          >>> abs(11 - (np.mean(observations) - mean_based_estimator(observations))) < 4
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
