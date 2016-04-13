test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure your table looks like the example one.  Consider the
          >>> # order of arguments to pivot.
          >>> 'Relationship Rating' in 'Relationship Rating' in ratings_by_gender.labels
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(ratings_by_gender.column('female'))
          [633, 318, 34, 32, 16]
          >>> list(ratings_by_gender.labels)
          ['Relationship Rating', 'female', 'male']
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
