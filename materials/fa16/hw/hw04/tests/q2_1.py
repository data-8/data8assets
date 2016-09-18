test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from datascience import *
          >>> type(reuters) == tables.Table
          True
          >>> reuters.num_columns
          1
          >>> 'Raw text' in reuters.labels
          True
          >>> # It looks like you're not splitting up the articles correctly.
          >>> 900 < reuters.num_rows < 1100
          True
          >>> # It looks like you're doing roughly the right thing, but
          >>> # you're not splitting up the articles in quite the right way,
          >>> # so you're getting a few extra articles.
          >>> reuters.num_rows <= 1000
          True
          >>> # It looks like you're doing roughly the right thing, but
          >>> # you're not splitting up the articles in quite the right way,
          >>> # so you're losing a few articles.
          >>> reuters.num_rows >= 1000
          True
          >>> reuters.num_rows
          1000
          >>> "***ARTICLE***".join(reuters.column(0)) == big_reuters_string
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
