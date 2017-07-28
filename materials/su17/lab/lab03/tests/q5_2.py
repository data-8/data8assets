test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ninety_nine.num_rows == 5
          True
          >>> ninety_nine.sort(0)
          Votes   | Rating | Title           | Year | Decade
          630994  | 8.1    | The Sixth Sense | 1999 | 1990
          672878  | 8.5    | The Green Mile  | 1999 | 1990
          735056  | 8.4    | American Beauty | 1999 | 1990
          1073043 | 8.7    | The Matrix      | 1999 | 1990
          1177098 | 8.8    | Fight Club      | 1999 | 1990
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
