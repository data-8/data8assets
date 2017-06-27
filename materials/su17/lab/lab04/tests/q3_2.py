test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You either didn't add the 'Total Pay ($)' column, or 
          >>> # you mislabeled it
          >>> 'Total Pay ($)' in compensation.column_labels
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You have the column in your table, but the values may be wrong
          >>> t = compensation.sort('Total Pay ($)', descending = True)
          >>> t.column('Total Pay ($)').item(0) == 53250000.0
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
