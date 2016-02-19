test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Please set box_22 to something.
          >>> box_22 is not None
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You've miscounted the number of cats.  Count faces.
          >>> cat_box_hash(box_22) not in [775115, 13219744, 3821276218]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Box doesn't expect a list [] as its argument; pass it
          >>> # several arguments if you want a Box with several things
          >>> # in it.
          >>> cat_box_hash(box_22) != 1054479096733125344
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> cat_box_hash(box_22) == 224778437
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
