test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(fizzbuzz(4))
          <class 'str'>
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> fizzbuzz(10)
          'buzz'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> fizzbuzz(9)
          'fizz'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> fizzbuzz(30)
          'fizzbuzz'
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
