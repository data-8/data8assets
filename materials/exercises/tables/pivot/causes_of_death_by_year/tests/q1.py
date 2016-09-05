test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you switched the order of the arguments to pivot.
          >>> "1999" not in causes_by_year.labels
          True
          >>> # It looks like you pivoted, but you need to tell pivot to sum
          >>> # up all the Count values.  Right now it's just counting up the
          >>> # number of rows for each year-cause pair, which just gives 
          >>> # the number of ZIP codes in the dataset.
          >>> causes_by_year.column("ALZ").item(0) != 1515
          True
          >>> causes_by_year.sort("Year").select(sorted(causes_by_year.labels)).take(range(5))
          ALZ  | CAN   | CLD   | DIA  | HOM  | HTD   | HYP  | INJ   | LIV  | NEP  | OTH   | PNF  | STK   | SUI  | Year
          3934 | 52880 | 13187 | 6004 | 2042 | 69900 | 0    | 8940  | 3546 | 0    | 38392 | 8014 | 18079 | 3047 | 1999
          4398 | 53005 | 12754 | 6203 | 2084 | 68533 | 0    | 8814  | 3673 | 0    | 39259 | 8355 | 18090 | 3113 | 2000
          4897 | 53810 | 13056 | 6457 | 2301 | 69004 | 2348 | 9274  | 3759 | 0    | 38383 | 8167 | 18078 | 3256 | 2001
          5405 | 53926 | 12643 | 6783 | 2459 | 68387 | 0    | 9882  | 3725 | 0    | 41177 | 8098 | 17551 | 3210 | 2002
          6585 | 54307 | 13380 | 7088 | 2481 | 69013 | 2578 | 10470 | 3832 | 0    | 40325 | 8184 | 17686 | 3396 | 2003
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
