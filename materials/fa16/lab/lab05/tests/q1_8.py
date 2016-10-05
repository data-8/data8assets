test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure your column labels are correct
          >>> estimates.labels == ('min estimate', 'mean-based estimate')
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> abs(14 - np.mean(estimates.column('min estimate'))) < .5
          True
          >>> abs(11.5 - np.mean(estimates.column('mean-based estimate'))) < .5
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
