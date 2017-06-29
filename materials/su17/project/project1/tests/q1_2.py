test = {
  'name': 'Question 1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Check your column labels and spelling
          >>> b_five_growth.labels == ('time', 'population_total', 'annual_growth')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> first = round(b_five_growth.sort(0).column(2).item(0), 8)
          >>> 0.005 <= first <= 0.5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You might be using the same values for initial and changed
          >>> all(np.round(b_five_growth.column(2), 4) == np.zeros(9))
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Compute the annual exponential growth rate
          >>> max(b_five_growth.column(2)) < 0.03
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Compute the annual exponential growth rate
          >>> np.allclose(np.round(sum(b_five_growth.column(2)), 5), 0.18323)
          True
          """,
          'hidden': True,
          'locked': False
        },
        {
          'code': r"""
          >>> # Table does not have expected values
          >>> round(b_five_growth.column(2).item(0), 8) == 0.01837042
          True
          >>> round(b_five_growth.column(2).item(3), 8) == 0.02644713
          True
          >>> round(b_five_growth.column(2).item(8), 8) == 0.01207657
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
