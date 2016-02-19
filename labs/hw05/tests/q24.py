test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Please set box_24 to something.
          >>> box_24 is not None
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Your box is empty!
          >>> cat_box_hash(box_24) != 17
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Consider the second cat.
          >>> cat_box_hash(box_24) != 775115
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> cat_box_hash(box_24) == 211685292
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
