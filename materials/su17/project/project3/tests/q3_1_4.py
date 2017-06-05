test = {
  'name': 'Question 3.1.4',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> genre_and_distances.take(np.arange(5)).group('Genre').index_by('Genre')[my_assigned_genre][0].item('count') >= 3
          True
          >>> my_assigned_genre_was_correct == (my_assigned_genre == 'Country')
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
