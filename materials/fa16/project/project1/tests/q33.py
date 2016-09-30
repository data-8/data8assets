test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> district_for_zip(94709)
          '0110005'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> district_for_zip(91106)
          '1910124'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> district_for_zip(94107)
          '3810011'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> district_for_zip(90023)
          'No District'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you forgot to sort by "District in ZIP".
          >>> district_for_zip(95628)
          '3410021'
          """,
          'hidden': False,
          'locked': False
        },        
        {
          'code': r"""
          >>> district_for_zip(11111)
          'No District'
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
