test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> elections.labels
          ('year', 'state', 'south', 'democrat')
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(elections.column('year') == full.column('year'))
          True
          >>> all(elections.column('state') == full.column('state'))
          True
          >>> all(elections.column('south') == full.column('south'))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> elections.column('democrat').item(1) == 0.6703
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(elections.column('democrat') <= 1)
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
