from linguee import Linguee
from collins import Collins

destination = 'en'  # Language you will translate the unknown word to
source = 'de'  # Language you are learning
language = 'german'  # Same as source language as expected by Collins website

linguee = Linguee()
collins = Collins()

ask = input('Enter the word: ')


def ask_in_tl(ask):
    """Takes the word, checks if it is already in the list. If not in the list, looks for sample sentences in Linguee and checks the word frequency in Collins"""
    check = False
    if source == 'de':
        check = linguee.check_in_list(ask)
    linguee.get_examples(ask, source, destination)
    if check != True:
        collins.check_frequency(ask, language)
    linguee.reset()


ask_in_tl(ask)
