test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Create chord_pressures by adding together the pressure arrays
          >>> # for the 3 notes.
          >>> all(chord_pressures == a_pressures + c_sharp_pressures + e_pressures)
          True
          >>> # chord_sound should be the name given to the output of a
          >>> # call to the function Audio.  So you should have a line of code
          >>> # that starts like this:
          >>> #   chord_sound = Audio(...)
          >>> import IPython.display
          >>> type(chord_sound) == IPython.display.Audio
          True
          >>> # It looks like you're using the wrong array as audio data.
          >>> chord_sound.data.startswith(b'RIFF\xbc\t\x04\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00D\xac\x00\x00\x88X\x01\x00\x02\x00\x10\x00data\x98\t\x04\x00\x00\x000\x05^\n\x87\x0f\xaa\x14\xc5\x19\xd4\x1e\xd6#\xc9(\xaa-x217\xd2;Z@\xc6D\x15IFMUQBU\x0bY\xaf\\+`\x7fc\xa9f\xa8i{l o\x96q\xdds\xf4u\xdaw\x8ey\x0f{^|y}`~\x13\x7f\x93\x7f\xde\x7f\xf5\x7f\xd8\x7f\x87\x7f\x03\x7fK~a}E|\xf7zyy\xcaw\xedu\xe2s\xaaqFo\xb7l\xffi\x1fg\x18d\xed`\x9d],Z\x9aV\xeaR\x1dO4K3G\x19C\xeb>\xa8:T6\xf01~-\x01)y$\xea\x1fU\x1b\xbd')
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
