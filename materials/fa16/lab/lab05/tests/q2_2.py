test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure you're making a copy of jury with extra columns
          >>> with_proportions.num_rows == 2
          True
          >>> with_proportions.num_columns == 5
          True
          >>> jury.num_columns == 3
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> (with_proportions.column(3) == make_array(.26, .74)).all() or (with_proportions.column(4) == make_array(.26, .74)).all()
          True
          >>> (with_proportions.column(4) == make_array(0.08, 0.92)).all() or (with_proportions.column(3) == make_array(0.08, 0.92)).all()
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
