test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all(np.array(sorted([v[1]._attrs['popup'] for v in labeled_map.items()])[0:5]) == ['Adelanto Stadium Farmers Market', "Alameda Farmers' Market", "Alisal Certified Farmers' Market", "Altadena Farmers' Market", "Alum Rock Village Farmers' Market"])
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
