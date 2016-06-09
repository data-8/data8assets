test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # If you're stuck, here's the answer:
          >>> #   murder_rates.join("State", death_penalty, "State")
          >>> print(murder_rates_with_death_penalty.take(range(10)))
          State   | Year | Population | Murder Rate | Death Penalty
          Alabama | 1960 | 3266740    | 12.4        | Death penalty
          Alabama | 1961 | 3302000    | 12.9        | Death penalty
          Alabama | 1962 | 3358000    | 9.4         | Death penalty
          Alabama | 1963 | 3347000    | 10.2        | Death penalty
          Alabama | 1964 | 3407000    | 9.3         | Death penalty
          Alabama | 1965 | 3462000    | 11.4        | Death penalty
          Alabama | 1966 | 3517000    | 10.9        | Death penalty
          Alabama | 1967 | 3540000    | 11.7        | Death penalty
          Alabama | 1968 | 3566000    | 11.8        | Death penalty
          Alabama | 1969 | 3531000    | 13.7        | Death penalty
          """,
          'hidden': False,
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
