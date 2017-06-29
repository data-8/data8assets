test = {
  'name': 'Question 3.2.3',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> check(0)
          True
          >>> check(1)
          True
          >>> check(2)
          True
          >>> check(3)
          True
          >>> check(4)
          True
          >>> check(5)
          True
          >>> check(6)
          True
          >>> check(7)
          True
          >>> check(8)
          True
          >>> check(9)
          True
          >>> check(10)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': r"""
      def check(r):
          t = test_20.row(r)
          return classify(t, train_20, train_lyrics.column('Genre'), 5) == simple_classify(t)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
