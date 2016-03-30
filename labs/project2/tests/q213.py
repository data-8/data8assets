test = {
  'name': '2.1.3',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> f = distance_from("In Your Eyes", "like", "love")
          >>> dis = f("Insane In The Brain")
          >>> np.isclose(dis, 0.0601087823407)
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
