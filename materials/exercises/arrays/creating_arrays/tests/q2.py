test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> # It looks like you didn't make an array.
          >>> type(book_title_words) == np.ndarray
          True
          >>> # It looks like you included commas in the text.
          >>> # The three pieces of text in the array should be:
          >>> #   "Eats"
          >>> #   "Shoots"
          >>> #   "and Leaves"
          >>> not any([',' in text for text in book_title_words])
          True
          >>> # It looks like you didn't include both words in the
          >>> # last piece of text.  It should be the actual string:
          >>> #   "and Leaves"
          >>> 'and ' in book_title_words.item(2)
          True
          >>> book_title_words
          array(['Eats', 'Shoots', 'and Leaves'], 
                dtype='<U10')
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
