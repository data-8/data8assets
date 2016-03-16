test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you're using the training set, but we wanted
          >>> # to use the test set here.
          >>> len(just_size_test_predictions) != 300
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(just_size_test_predictions)
          266
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(np.mean(just_size_test_predictions))
          321851.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(np.std(just_size_test_predictions))
          152160.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(just_size_test_errors)
          266
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(np.mean(just_size_test_errors))
          8560.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(np.std(just_size_test_errors))
          135533.0
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
