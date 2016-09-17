test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def is_mlk(street):
          ...   return "martin luther" in street.lower() or "mlk" in street.lower()
          >>> def is_center(street):
          ...   return "center" in street.lower()
          >>> is_mlk(north_south_street) and is_center(east_west_street) or is_mlk(east_west_street) and is_center(north_south_street)
          True
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
