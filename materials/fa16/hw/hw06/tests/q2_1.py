test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from datascience import *
          >>> type(with_state) == tables.Table
          True
          >>> with_state.num_columns
          8
          >>> with_state.num_rows
          7156
          >>> with_state.select(sorted(with_state.labels)).take(range(5))
          Address                        | City       | Institution ID | Name                                | Number of Pell grant recipients | Number of undergraduates | State (abbreviated) | ZIP
          4900 Meridian Street           | Normal     | 100654         | Alabama A & M University            | 2967                            | 4170                     | AL                  | 35762
          Administration Bldg Suite 1070 | Birmingham | 100663         | University of Alabama at Birmingham | 3958                            | 11291                    | AL                  | 35294-0110
          1200 Taylor Rd                 | Montgomery | 100690         | Amridge University                  | 225                             | 329                      | AL                  | 36117-3553
          301 Sparkman Dr                | Huntsville | 100706         | University of Alabama in Huntsville | 1930                            | 5882                     | AL                  | 35899
          915 S Jackson Street           | Montgomery | 100724         | Alabama State University            | 4240                            | 5130                     | AL                  | 36104-0271""",
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
