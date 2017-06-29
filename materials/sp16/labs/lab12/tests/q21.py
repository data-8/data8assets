test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t = Table(['Condition', 'Value']).with_rows([['A', 2], ['B', 3], ['A', 3]])
          >>> permutation_test(t, 'Condition', 'Value', tvd)
          Observation: 0.5
          Empirical P-value: 1.0
          >>> permutation_test(t, 'Condition', 'Value', lambda a, b, c: tvd(a, b, c) * 4)
          Observation: 2.0
          Empirical P-value: 1.0
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
