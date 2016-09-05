test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from datascience import *
          >>> type(schools_with_attendance) == tables.Table
          True
          >>> schools_with_attendance.num_columns
          10
          >>> schools_with_attendance.num_rows
          151
          >>> schools_with_attendance.sort('Number of full-time undergraduates', descending=True).take(range(5))
          Institution ID | Name                              | City          | State | ZIP        | CSA  | County               | Longitude | Latitude | Number of full-time undergraduates
          110635         | University of California-Berkeley | Berkeley      | CA    | 94720      | 488  | Alameda County       | -122.26   | 37.8715  | 27568
          122597         | San Francisco State University    | San Francisco | CA    | 94132      | 488  | San Francisco County | -122.478  | 37.7213  | 22077
          122755         | San Jose State University         | San Jose      | CA    | 95192-0001 | 488  | Santa Clara County   | -121.881  | 37.3352  | 20414
          112190         | City College of San Francisco     | San Francisco | CA    | 94112-1898 | 488  | San Francisco County | -122.451  | 37.726   | 17569
          113333         | De Anza College                   | Cupertino     | CA    | 95014      | 488  | Santa Clara County   | -122.045  | 37.3192  | 16729
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
