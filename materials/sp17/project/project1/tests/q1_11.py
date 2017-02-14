test = {
  'name': 'Question 1_11',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Incorrect labels for columns
          >>> t = stats_for_year(1990)
          >>> t.labels == ('geo', 'population_total', 'children_per_woman_total_fertility', 'child_mortality_under_5_per_1000_born')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Incorrect number of rows
          >>> t = stats_for_year(1990)
          >>> t.num_rows
          50
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(stats_for_year(1960).sort('geo').take(np.arange(5, 50, 5)))
          geo  | population_total | children_per_woman_total_fertility | child_mortality_under_5_per_1000_born
          chn  | 644450173        | 3.99                               | 309
          egy  | 27072397         | 6.63                               | 312.8
          gha  | 6652285          | 6.75                               | 210.9
          ita  | 49714962         | 2.37                               | 52
          mex  | 38174114         | 6.78                               | 142.9
          npl  | 10056945         | 5.99                               | 327.1
          prk  | 11424179         | 4.58                               | 127.3
          tur  | 27553280         | 6.3                                | 249
          uzb  | 8789492          | 6.71                               | 175.7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(stats_for_year(2010).sort('geo').take(np.arange(3, 50, 5)))
          geo  | population_total | children_per_woman_total_fertility | child_mortality_under_5_per_1000_born
          bra  | 198614208        | 1.84                               | 16.7
          deu  | 80435307         | 1.39                               | 4.2
          fra  | 62961136         | 1.98                               | 4.3
          irn  | 74253373         | 1.9                                | 19.2
          kor  | 49090041         | 1.27                               | 4.1
          mys  | 28119500         | 2                                  | 8.3
          phl  | 93038902         | 3.15                               | 31.9
          sdn  | 36114885         | 4.64                               | 80.2
          ukr  | 45647497         | 1.44                               | 11.8
          yem  | 23591972         | 4.5                                | 58.8
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
