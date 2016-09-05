test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # a_below_middle_c should be the name given to the output of a
          >>> # call to the function Audio.  So your code should start like
          >>> # this:
          >>> #   a_below_middle_c = Audio(...)
          >>> import IPython.display
          >>> type(a_below_middle_c) == IPython.display.Audio
          True
          >>> # It looks like you're using the wrong array as audio data.
          >>> a_below_middle_c.data.startswith(b'RIFF\xbc\t\x04\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00D\xac\x00\x00\x88X\x01\x00\x02\x00\x10\x00data\x98\t\x04\x00\x00\x00\x02\x04\x04\x08\x04\x0c\x01\x10\xfa\x13\xee\x17\xdb\x1b\xc2\x1f\xa1#w\'C+\x04/\xb92a6\xfc9\x88=\x05AqD\xcdG\x16KLNnQ|TuWXZ$]\xd9_ub\xf9dcg\xb4i\xeak\x04n\x03p\xe6q\xacsUu\xe1vNx\x9ey\xcfz\xe1{\xd3|\xa7}Z~\xee~c\x7f\xb7\x7f\xeb\x7f\xfe\x7f\xf2\x7f\xc5\x7fx\x7f\x0c\x7f\x7f~\xd2}\x06}\x1a|\x10{\xe6y\x9dx6w\xb2u\x0ftPrsp{nfl7j\xecg\x88e\ncs`\xc4]\xfdZ\x1fX+U"R\x04O\xd2K\x8dH6E\xceAU>\xcc:47')
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
