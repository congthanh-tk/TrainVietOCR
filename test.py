from spellchecker import SpellChecker

spell = SpellChecker(distance=1)

spell.word_frequency.load_text_file('Viet74K.txt')


# find those words that may be misspelled
misspelled = spell.unknown("X Bình Yên H. Đinh Hoá, T. Thái Nguyên".split(" "))

for word in misspelled:
    print(spell.word_probability(word))
    # Get the one `most likely` answer
    print(spell.correction(word))

    # Get a list of `likely` options
    print(spell.candidates(word))