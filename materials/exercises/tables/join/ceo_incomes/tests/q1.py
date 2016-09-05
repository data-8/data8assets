test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> compensation_and_company.sort("Company").take(range(5)).select('Company', 'First Name', 'Last Name', 'Headquarters', 'Total compensation ($)', 'Cash compensation ($)', 'Stock compensation ($)', 'Other compensation ($)', 'Change from previous year', 'Symbol', 'LastSale', 'MarketCap', 'IPOyear', 'Sector', 'industry', 'Summary Quote')
          Company                | First Name | Last Name | Headquarters | Total compensation ($) | Cash compensation ($) | Stock compensation ($) | Other compensation ($) | Change from previous year | Symbol | LastSale | MarketCap | IPOyear | Sector           | industry                                         | Summary Quote
          A-Mark Precious Metals | Gregory    | Roberts   | Santa Monica | 940000                 | 930000                | 0                      | 20000                  | -0.11                     | AMRK   | 17.01    | $119.02M  | n/a     | Basic Industries | Other Specialty Stores                           | http://www.nasdaq.com/symbol/amrk
          Activision Blizzard    | Robert     | Kotick    | Santa Monica | 7.23e+06               | 7.14e+06              | 0                      | 90000                  | 0.05                      | ATVI   | 41.25    | $30.59B   | n/a     | Technology       | Computer Software: Prepackaged Software          | http://www.nasdaq.com/symbol/atvi
          Adobe Systems          | Shantanu   | Narayen   | San Jose     | 1.836e+07              | 2.41e+06              | 1.585e+07              | 90000                  | 0.03                      | ADBE   | 98.87    | $49.27B   | 1986    | Technology       | Computer Software: Prepackaged Software          | http://www.nasdaq.com/symbol/adbe
          Advanced Micro Devices | Lisa       | Su        | Sunnyvale    | 6.56e+06               | 1.15e+06              | 5.38e+06               | 30000                  | 0                         | AMD    | 6.6      | $5.25B    | n/a     | Technology       | Semiconductors                                   | http://www.nasdaq.com/symbol/amd
          Agilent Technologies   | Michael    | McMullen  | Santa Clara  | 7.21e+06               | 1.96e+06              | 4.95e+06               | 300000                 | 0                         | A      | 47.45    | $15.45B   | 1999    | Capital Goods    | Biotechnology: Laboratory Analytical Instruments | http://www.nasdaq.com/symbol/a
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
