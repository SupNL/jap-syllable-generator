import sys
import argparse
import platform
import os
import random
import msvcrt as m

wiwe_syllables = ["wi", "we"]

dakuten_handakuten_syllables = [
    "ga", "gi", "gu", "ge", "go",
    "za", "ji", "zu", "ze", "zo",
    "da", "ji", "zu", "de", "do",
    "da", "ji", "zu", "de", "do",
    "pa", "pi", "pu", "pe", "po"
]

sokuon_syllables = [
    "kka", "kki", "kku", "kke", "kko",
    "ssa", "ssi", "ssu", "sse", "sso",
    "tta", "tti", "ttu", "tte", "tto"
]

sokuon_dakuten_handakuten_syllables = [
    "bba", "bbi", "bbu", "bbe", "bbo",
    "ppa", "ppi", "ppu", "ppe", "ppo"
]

combination_dakuten_handakuten_syllables = [
    "gya", "gyu", "gyo",
    "ja",  "ju",  "jo",
    "bya", "byu", "byo",
    "pya", "pyu", "pyo"
]

combination_syllables = [
    "kya", "kyu", "kyo",
    "sha", "shu", "sho",
    "cha", "chu", "cho",
    "nya", "nyu", "nyo",
    "hya", "hyu", "hyo",
    "mya", "myu", "myo",
    "rya", "ryu", "ryo"
]

syllables = [
    "a",  "i",  "u",  "e",  "o",
    "ka", "ki", "ku", "ke", "ko",
    "sa", "si", "su", "se", "so",
    "ta", "ti", "tu", "te", "to",
    "na", "ni", "nu", "ne", "no",
    "ha", "hi", "hu", "he", "ho",
    "ma", "mi", "mu", "me", "mo",
    "ya", "yu", "yo",
    "ra", "ri", "ru", "re", "ro",
    "wa",                   "wo",
    "n"
]


def treat_args(args):
    global syllables
    if args.dakuten:
        syllables.extend(dakuten_handakuten_syllables)
        combination_syllables.extend(combination_dakuten_handakuten_syllables)
        sokuon_syllables.extend(sokuon_dakuten_handakuten_syllables)
    if args.wiwe:
        syllables.extend(wiwe_syllables)
    if args.youon:
        syllables.extend(combination_syllables)
    if args.sokuon:
        syllables.extend(sokuon_syllables)
    if args.uppercase:
        syllables = [syllable.upper() for syllable in syllables]
    if type(args.size) == 'list':
        args.size = args.size[0]
    if args.space:
        return ' '
    return ''


def generate_random_word(space):
    for _ in range(args.size):
        print(random.choice(syllables), end='')
        print(space, end='')
    print(end='\n\n')
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dakuten", help="include syllables with dakuten (゛) and handakuten (゜)", action='store_true')
    parser.add_argument("-w", "--wiwe", help="include wi (ゐ) and we (ゑ) syllables", action='store_true')
    parser.add_argument("-u", "--uppercase", help="capitalize the syllables", action='store_true')
    parser.add_argument("-a", "--space", help="add space between syllables", action='store_true')
    parser.add_argument("-s", "--sokuon", help="include letters to represent sokuons (っ)", action='store_true')
    parser.add_argument("-y", "--youon", help="include combinations with 'ya' (ゃ), 'yu' (ゅ) and 'yo' (ょ)", action='store_true')
    parser.add_argument("-n", "--size", help="number of syllables per word", type=int, metavar="SIZE", default=5, action='store', nargs=1)
    args = parser.parse_args()

    space = treat_args(args)

    if platform.system() == 'Linux':
        clear = lambda: os.system('clear')
    else:
        clear = lambda: os.system('cls')

    while True:
        clear()
        print(f'Displaying words with {args.size} random syllables', end='\n\n')
        word = generate_random_word(space)
        print('Press q to quit, or anything else to generate a new word')
        command = bytes.decode(m.getch())
        if command == 'q':
            break;
        elif command == '\x03':
            raise KeyboardInterrupt
        


    
