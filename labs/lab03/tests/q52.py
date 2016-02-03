test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> names_only.labels
          ('First Name', 'Last Name')
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> names_only
          First Name | Last Name
          Fahad      | Kamran
          Melissa    | Chen
          Ruta       | Joshi
          Sam        | Lau
          Delphine   | Ho
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
