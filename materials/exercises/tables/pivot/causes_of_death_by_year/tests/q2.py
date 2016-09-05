test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> cleaned_causes_by_year.sort("Year").select(sorted(cleaned_causes_by_year.labels)).take(range(5))
          ALZ  | CAN   | CLD   | DIA  | HTD   | INJ   | LIV  | OTH   | PNF  | STK   | SUI  | Year
          3934 | 52880 | 13187 | 6004 | 69900 | 8940  | 3546 | 38392 | 8014 | 18079 | 3047 | 1999
          4398 | 53005 | 12754 | 6203 | 68533 | 8814  | 3673 | 39259 | 8355 | 18090 | 3113 | 2000
          4897 | 53810 | 13056 | 6457 | 69004 | 9274  | 3759 | 38383 | 8167 | 18078 | 3256 | 2001
          5405 | 53926 | 12643 | 6783 | 68387 | 9882  | 3725 | 41177 | 8098 | 17551 | 3210 | 2002
          6585 | 54307 | 13380 | 7088 | 69013 | 10470 | 3832 | 40325 | 8184 | 17686 | 3396 | 2003
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
