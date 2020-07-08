# Random syllables generator to practice japanese writing

## NOTE: **THIS DOES NOT GENERATE RANDOM KANAS!** It generates random syllables in latin alphabet letters, so it can be transcribed to katakana or hiragana by the user.

---

## Dependencies

* Python 3 or higher

---

## Running the program

If you're on windows, run the program with:

    py pyjb.py

If it won't recognize your python, define it on PATH or reference the .exe with:

    C:\path\to\python.exe pyjb.py

If you're on Linux, run with:

    python3 pyjb.py

It should display a random word, like below:

    Displaying words with 5 random syllables

    tamorenasi

    Press q to quit, or anything else to generate a new word

---

## Usage

Directly from the console:

    usage: pyjp.py [-h] [-d] [-w] [-u] [-a] [-s] [-y] [-n SIZE]

    optional arguments:  
      -h, --help            show this help message and exit  
      -d, --dakuten         include syllables with dakuten (゛) and handakuten (゜)
      -w, --wiwe            include wi (ゐ) and we (ゑ) syllables
      -u, --uppercase       capitalize the syllables
      -a, --space           add space between syllables
      -s, --sokuon          include letters to represent sokuons (っ)
      -y, --youon           include combinations with 'ya' (ゃ), 'yu' (ゅ) and 'yo' (ょ)
      -l, --literal         ignore the way the syllable is pronunciated (for
                        example, tsu become tu, and chi become ti)
      -n SIZE, --size SIZE  number of syllables per word

## Include Dakuten and Handakuten

Arguments: -d or --dakuten

Include syllables that represent kanas with dakuten (゛) and handakuten (゜).

## Include Wi and We syllables

Arguments: -w or --wiwe

Since ゐ (wi) and ゑ (we) are considered nearly obsoletes kana, those may be optionally turned on.

## Uppercase syllables

Arguments: -u or --uppercase

Makes all syllables to be uppercase.

## Space between syllables

Arguments: -a or --space

Add space between syllables.

## Include Sokuons

Arguments: -s or --sokuon

Add syllables to represent the sokuon (っ), for example, kki (っき). If dakuten and handakuten are enabled, also include for those.

## Include Yōon

Arguments: -y or --youon

Add syllables to represent the yōon (kana that is combined with ゃ, ゅ and ょ), for example, kya (きゃ). If dakuten and handakuten are enabled, also include for those.

## Word size

Arguments: -n SIZE or --size SIZE, where SIZE is the number

Number of syllables to be added on a word.