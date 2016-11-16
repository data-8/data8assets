test = {
  'name': 'Question 2.1.2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure you can use any two songs
          >>> correct_dis = 0.043273487774941777
          >>> dis = distance_two_features("Lookin' for Love", "Insane In The Brain", "like", "love")
          >>> np.isclose(dis, correct_dis)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure you can use any two features
          >>> correct_dis = 0.037895701438882219
          >>> dis = distance_two_features("In Your Eyes", "Sangria Wine", "the", "of")
          >>> np.isclose(dis, correct_dis)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': r"""
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
