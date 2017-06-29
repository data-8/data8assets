test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> train.num_rows
          300
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(train.take(range(3)))
          Price  | Bedrooms | Bathrooms | Size | Santa Maria-Orcutt (0/1) | Paso Robles (0/1) | Atascadero (0/1) | Nipomo (0/1) | Arroyo Grande (0/1) | Lompoc (0/1) | Los Osos (0/1) | Grover Beach (0/1) |  Paso Robles (0/1) | San Miguel (0/1)
          232600 | 3        | 3         | 1582 | 1                        | 0                 | 0                | 0            | 0                   | 0            | 0              | 0                  | 0                  | 0
          119000 | 1        | 1         | 900  | 1                        | 0                 | 0                | 0            | 0                   | 0            | 0              | 0                  | 0                  | 0
          220000 | 3        | 2         | 1112 | 0                        | 0                 | 0                | 1            | 0                   | 0            | 0              | 0                  | 0                  | 0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> test.num_rows
          266
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(test.take(range(3)))
          Price  | Bedrooms | Bathrooms | Size | Santa Maria-Orcutt (0/1) | Paso Robles (0/1) | Atascadero (0/1) | Nipomo (0/1) | Arroyo Grande (0/1) | Lompoc (0/1) | Los Osos (0/1) | Grover Beach (0/1) |  Paso Robles (0/1) | San Miguel (0/1)
          129900 | 3        | 1         | 1042 | 1                        | 0                 | 0                | 0            | 0                   | 0            | 0              | 0                  | 0                  | 0
          199900 | 4        | 2         | 1338 | 0                        | 0                 | 0                | 0            | 0                   | 1            | 0              | 0                  | 0                  | 0
          449900 | 4        | 3         | 3035 | 0                        | 0                 | 0                | 0            | 0                   | 1            | 0              | 0                  | 0                  | 0
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
