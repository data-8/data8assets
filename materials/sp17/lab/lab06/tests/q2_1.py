test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> old = full_data.with_column('Age', full_data.column('Age')*3)
          >>> np.max(age_bins(old)) == np.max(old.column('Age')) + 1
          True
          >>> np.min(age_bins(old)) == np.min(old.column('Age'))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.max(salary_bins(full_data)) > np.max(full_data.column('Salary'))
          True
          >>> np.min(salary_bins(full_data)) == np.min(full_data.column('Salary'))
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
