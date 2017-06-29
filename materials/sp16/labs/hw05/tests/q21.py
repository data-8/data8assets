test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Please set box_21 to something.
          >>> box_21 is not None
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # What is the cat inside?
          >>> cat_box_hash(box_21) != 149
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # How did you see the box but miss the cat??
          >>> cat_box_hash(box_21) != 17
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
          >>> cat_box_hash(box_21) != 96283387448126112
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> cat_box_hash(box_21) == 43078
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
