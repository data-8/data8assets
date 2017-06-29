test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = print_and_return("The GSIs of Data 8 are the best!")
          The GSIs of Data 8 are the best!
          >>> x
          32
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '#print = lambda *args: None\n' + 'import doctest',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
