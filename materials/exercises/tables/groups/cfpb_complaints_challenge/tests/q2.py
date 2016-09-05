test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from datascience import tables
          >>> type(complaints_against_big_companies) == tables.Table
          True
          >>> complaints_against_big_companies.num_rows
          2987
          >>> complaints_against_big_companies.take(range(5))
          company         | company_public_response                                      | company_response        | complaint_id | complaint_what_happened                                      | consumer_consent_provided | consumer_disputed | date_received           | date_sent_to_company    | issue                                    | product                 | state | sub_issue | sub_product                 | submitted_via | tags   | timely | zip_code
          Bank of America | Company has responded to the consumer and the CFPB and c ... | Closed with explanation | 1907306      | I became aware of several charges on a Bank of America c ... | Consent provided          | No                | 2016-05-03T16:49:33.000 | 2016-05-03T16:49:34.000 | Other                                    | Credit card             | VA    | (None)    | (None)                      | Web           | (None) | Yes    | 239XX
          Bank of America | Company has responded to the consumer and the CFPB and c ... | Closed with explanation | 1904918      | (None)                                                       | (None)                    | No                | 2016-05-02T12:58:03.000 | 2016-05-04T15:15:29.000 | Deposits and withdrawals                 | Bank account or service | TX    | (None)    | Checking account            | Referral      | (None) | Yes    | 75050
          Bank of America | Company has responded to the consumer and the CFPB and c ... | Closed with explanation | 1913749      | (None)                                                       | (None)                    | No                | 2016-05-06T22:02:18.000 | 2016-05-11T13:17:03.000 | Loan servicing, payments, escrow account | Mortgage                | NV    | (None)    | Other mortgage              | Referral      | (None) | Yes    | 89002
          Bank of America | Company has responded to the consumer and the CFPB and c ... | Closed with explanation | 1940854      | Bank of America has deleted my mortgage credit line from ... | Consent provided          | Yes               | 2016-05-25T19:25:30.000 | 2016-06-01T18:59:09.000 | Credit decision / Underwriting           | Mortgage                | TX    | (None)    | Conventional fixed mortgage | Web           | (None) | Yes    | 750XX
          Bank of America | Company has responded to the consumer and the CFPB and c ... | Closed with explanation | 1910227      | (None)                                                       | (None)                    | No                | 2016-05-04T17:06:12.000 | 2016-05-09T12:11:01.000 | Making/receiving payments, sending money | Bank account or service | NY    | (None)    | Other bank product/service  | Postal mail   | (None) | Yes    | 11422
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
