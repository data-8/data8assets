test = {
  'name': 'Question 1_7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure you are using the date range 1970-2015
          >>> fertility_and_child_mortality.num_rows
          46
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Check your column labels and spelling
          >>> all([label in fertility_and_child_mortality.labels for label in ['Children per woman', 'Child deaths per 1000 born']])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> facm = fertility_and_child_mortality.select('Children per woman', 'Child deaths per 1000 born')
          >>> np.allclose(facm.column(1).item(0), 224.1)
          True
          >>> np.allclose(facm.column(1).item(-1), 37.6)
          True
          >>> np.allclose(facm.column(0).item(-1), 2.12)
          True
          >>> np.allclose(facm.column(0).item(0), 6.95)
          True
          >>> np.allclose(facm.column(1).mean(), 131.41521739130437)
          True
          >>> np.allclose(facm.column(0).mean(), 4.3958695652173922)
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
