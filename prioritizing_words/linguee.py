import requests
import csv
from difflib import SequenceMatcher, get_close_matches

LINGUEE_API = 'https://linguee-api.fly.dev/api/v2/translations'

class Linguee:
    def __init__(self):
        self.dictionary = {}
        self.translations = []
        self.translations_w_examples = []
        self.examples_src = []
        self.examples_dst = []

    def reset(self):
        self.dictionary = {}
        self.translations = []
        self.translations_w_examples = []
        self.examples_src = []
        self.examples_dst = []

    def check_in_list(self, word):
        """Takes a word as an input and checks if it already is included in the list of words"""
        list = []
        with open('reformatedAnki_4000words.csv', encoding="utf-8-sig") as wordlist:
            for row in wordlist:
                list.append(row.split(',')[0])
        if word in list:
            print('This word is already in your list.')
            return True
        elif len(get_close_matches(word, list, cutoff=0.5)) > 0:
            #If no exactly matching words found, the programm looks for similar words
            confirm = input('Did you mean any of "%s" instead? Type "Y", "N", or number: ' % get_close_matches(word, list, cutoff=0.5))
            if confirm.lower() == 'y':
                if get_close_matches(word, list)[0] in list:
                    print('This word is already in your list.')
                    return True
            elif confirm.lower() != 'n':
                number = int(confirm)
                if get_close_matches(word, list)[number] in list:
                    print('This word is already in your list.')
                    return True

        else:
            pass

    def get_examples(self, input_word, source, dest):
        """Get sample sentences for a word from Linguee API"""
        body= {
            'query': input_word,
            'src':source,
            'dst':dest,
            'guess_direction': False
        }
        response = requests.get(url=LINGUEE_API, params=body)
        try:
            data = response.json()
            main_list = data
        except:
            print('No data found in Linguee.')
        else:
            try:
                if type(data) is list:
                    for version in main_list:
                        for point in version['translations']:
                            self.dictionary[point['text']] = point['examples']

                    for key,value in self.dictionary.items():
                        self.translations.append(key)
                        if len(value)>0:
                            self.translations_w_examples.append(key)
                            self.examples_src.append(value[0]['src'])
                            self.examples_dst.append(value[0]['dst'])

                    if len(self.translations_w_examples) !=0:
                        print("\nResults (translation, sample sentence, sample sentence translation):")
                        for _ in zip(self.translations_w_examples,self.examples_src, self.examples_dst):
                           print(_)
                    else:
                        print(f'\nPossible translations: {self.translations[:3]}')

                    self.reset()
                else:
                    print(f'The server is down, here is the server response {data}')
            except:
                print(f"Error, here is the server response {data}")





