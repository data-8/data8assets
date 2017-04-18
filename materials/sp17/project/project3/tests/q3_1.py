test = {
  'name': 'Question 3.1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0.1 <= distance_first_to_first <= 0.2
          True
          >>> np.isclose(distance(make_array(1, 2), make_array(1, 2)), 0)
          True
          >>> np.isclose(distance(make_array(1, 2, 3), make_array(2, 4, 5)), 3)
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
