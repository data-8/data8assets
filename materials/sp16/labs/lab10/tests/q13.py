test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your classifier isn't a function.
          >>> import collections
          >>> isinstance(my_classifier, collections.Callable)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you're not making the right classifier.  Are
          >>> # you calling make_classifier?
          >>> np.all(lyrics.drop(0).take(range(40, 45)).apply(my_classifier) == np.array(['Hip-hop', 'Country', 'Country', 'Hip-hop', 'Hip-hop']))
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
