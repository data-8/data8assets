test = {
  'name': 'Question 2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Please don't edit the last line.
          >>> latest.labels == ('geo', 'time', 'poverty_percent')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The result should have one row per country.
          >>> latest.num_rows
          145
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(latest.sort('geo').take(np.arange(7, 107, 10)))
          geo  | time | poverty_percent
          bdi  | 2006 | 81.32
          bra  | 2012 | 3.75
          cod  | 2006 | 87.72
          dom  | 2012 | 2.25
          fsm  | 2000 | 31.15
          guy  | 1998 | 8.7
          isr  | 2010 | 0.39
          lbr  | 2007 | 83.76
          mex  | 2012 | 1.03
          nga  | 2010 | 62.03
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
