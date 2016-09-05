test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from datascience import *
          >>> type(sfba_schools) == tables.Table
          True
          >>> sfba_schools.num_columns
          9
          >>> sfba_schools.num_rows
          161
          >>> sfba_schools.take(range(5))
          Institution ID | Name                                           | City          | State | ZIP        | CSA  | County               | Longitude | Latitude
          108232         | Academy of Art University                      | San Francisco | CA    | 94105      | 488  | San Francisco County | -122.401  | 37.7877
          108269         | Academy of Chinese Culture and Health Sciences | Oakland       | CA    | 94612      | 488  | Alameda County       | -122.273  | 37.8067
          108649         | Avalon School of Cosmetology-Alameda           | Alameda       | CA    | 94501      | 488  | Alameda County       | -122.244  | 37.7642
          108667         | College of Alameda                             | Alameda       | CA    | 94501      | 488  | Alameda County       | -122.279  | 37.7824
          108861         | American Baptist Seminary of the West          | Berkeley      | CA    | 94704-3029 | 488  | Alameda County       | -122.256  | 37.8653
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
