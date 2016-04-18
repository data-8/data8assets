test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> two_year_changes([10, 7, 12, 9, 13, 9, 11])
          2
          >>> two_year_changes(ak.column('Alaska'))
          -5
          >>> two_year_changes(mn.column('Minnesota'))
          6
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
