test = {
  'name': 'Question 1.3',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(most_murderous(1970).item(0), str)
          True
          >>> len(most_murderous(1970))
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(most_murderous(1970))
          ['North Carolina', 'Alaska', 'Florida', 'South Carolina', 'Georgia']
          >>> list(most_murderous(1990))
          ['California', 'Mississippi', 'Texas', 'New York', 'Louisiana']
          """,
          'hidden': True,
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
