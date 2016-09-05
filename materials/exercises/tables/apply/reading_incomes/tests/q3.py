test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # *Hint:* You'll need to define a function and use apply.
          >>> # If you call the function fix_pay, the call to apply could look
          >>> # something like this:
          >>> #   raw_compensation.select("Name")\
          >>> #                   .with_column("Total Pay ($)", raw_compensation.apply(fix_pay, "Total Pay")
          >>> # To start, try defining fix_pay as a function that just returns
          >>> # its argument, and see what happens.
          >>> from datascience import tables
          >>> type(pay_in_dollars) == tables.Table
          True
          >>> # Consider the string method `strip`.  For example, the value of
          >>> #   'jeep'.strip('j')
          >>> # is 'eep'.
          >>> pay_in_dollars.column("Total Pay ($)").item(0) != "$53.25 "
          True
          >>> # Consider the function float, which converts a string that looks
          >>> # like a number to an actual number.
          >>> pay_in_dollars.column("Total Pay ($)").item(0) == 53.25 * 10**6
          True
          >>> pay_in_dollars.select("Name", "Total Pay ($)").sort("Name").take(range(5))
          Name              | Total Pay ($)
          Aart J. de Geus*  | 4.92e+06
          Alain Monie       | 9.03e+06
          Andrew Wilson     | 1.163e+07
          Anthony F. Earley | 1.22e+07
          Arthur Peck       | 6.14e+06
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
