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
          >>> with_state.take(range(5))
          Institution ID | Number of Pell grant recipients | Number of undergraduates | Name                                | Address                        | City       | State (abbreviated) | ZIP
          100654         | 2967                            | 4170                     | Alabama A & M University            | 4900 Meridian Street           | Normal     | AL                  | 35762
          100663         | 3958                            | 11291                    | University of Alabama at Birmingham | Administration Bldg Suite 1070 | Birmingham | AL                  | 35294-0110
          100690         | 225                             | 329                      | Amridge University                  | 1200 Taylor Rd                 | Montgomery | AL                  | 36117-3553
          100706         | 1930                            | 5882                     | University of Alabama in Huntsville | 301 Sparkman Dr                | Huntsville | AL                  | 35899
          100724         | 4240                            | 5130                     | Alabama State University            | 915 S Jackson Street           | Montgomery | AL                  | 36104-0271
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
