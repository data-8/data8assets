test = {
  'name': 'Question 1.4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You might have flipped the difference.
          >>> ca_change > 0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You might have flipped the difference.
          >>> np.isclose(np.round(ca_change), 726)
          True
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
