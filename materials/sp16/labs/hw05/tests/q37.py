test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You didn't make estimates a Table.
          >>> isinstance(estimates, tables.Table)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You didn't run 1000 simulations.
          >>> estimates.num_rows == 1000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Your estimates table doesn't have the right columns.
          >>> set(estimates.labels) == set(["mean_based_estimate", "max_estimate"])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You probably aren't using the right random process, or
          >>> # you aren't using max to estimate N for the max_estimate column.
          >>> max(estimates.column("max_estimate")) == 120
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You probably aren't using the right random process, or
          >>> # you aren't using max to estimate N for the max_estimate column.
          >>> np.percentile(estimates.column("max_estimate"), 1) >= 73
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You probably aren't using the right random process, or
          >>> # you aren't using max to estimate N for the max_estimate column.
          >>> np.percentile(estimates.column("max_estimate"), 1) <= 95
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You probably aren't using the right random process, or
          >>> # you aren't using mean_based_estimator to estimate N for
          >>> # the mean_based_estimate column.
          >>> np.percentile(estimates.column("mean_based_estimate"), 1) >= 66
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You probably aren't using the right random process, or
          >>> # you aren't using mean_based_estimator to estimate N for
          >>> # the mean_based_estimate column.
          >>> np.percentile(estimates.column("mean_based_estimate"), 1) <= 85
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You probably aren't using the right random process, or
          >>> # you aren't using mean_based_estimator to estimate N for
          >>> # the mean_based_estimate column.
          >>> np.percentile(estimates.column("mean_based_estimate"), 99) >= 150
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You probably aren't using the right random process, or
          >>> # you aren't using mean_based_estimator to estimate N for
          >>> # the mean_based_estimate column.
          >>> np.percentile(estimates.column("mean_based_estimate"), 99) <= 175
          True
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