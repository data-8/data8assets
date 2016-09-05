test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> corrected_essays
          Name                                    | Corrected text
          a_desk_book_of_errors_in_english.txt    | 
          Project Gutenberg's A Desk-Book of Errors in English, b ...
          how_to_write_letters.txt                | 
          The Project Gutenberg EBook of How to Write Letters (Fo ...
          lippincotts_horn_ashbaugh_speller.txt   | 
          The Project Gutenberg EBook of Lippincott's Horn-Ashbau ...
          news_writing.txt                        | The Project Gutenberg EBook of News Writing, by M. Lyle  ...
          the_letters_of_henry_james_volume_I.txt | 
          Project Gutenberg's The Letters of Henry James (volume  ...
          the_virginian.txt                       | 
          The Project Gutenberg EBook of The Virginian, by Owen W ...
          >>> # It looks like the misspellings weren't corrected.
          >>> "mispel" not in corrected_essays.column("Corrected text").item(0)
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
