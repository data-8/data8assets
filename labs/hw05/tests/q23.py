test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Please set box_23 to something.
          >>> box_23 is not None
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Consider the number of boxes.  What is inside
          >>> # the outermost box?
          >>> cat_box_hash(box_23) != 43078
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Recount the number of boxes.
          >>> cat_box_hash(box_23) not in [12449559, 1039799622169]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> cat_box_hash(box_23) == 3597922568
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
