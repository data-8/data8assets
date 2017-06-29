test = {
  'name': 'Question 2.1.5',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> [most_common('Genre', close_songs.take(range(k))) for k in range(1, 8, 2)]
          ['Hip-hop', 'Hip-hop', 'Hip-hop', 'Country']
          >>> [most_common('Genre', close_songs.take(range(7-k, 7))) for k in range(1, 8, 2)]
          ['Country', 'Country', 'Country', 'Country']
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': """
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
