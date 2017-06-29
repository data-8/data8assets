test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> xy_points.num_columns
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(xy_points.column('x') == np.arange(5))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(xy_points.column('y') == np.arange(2, 11, 2))
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
