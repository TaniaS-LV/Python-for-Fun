import requests
import pandas as pd

# -------------------- Settings to change  --------------------------------
TARGET_LANGUAGE = 'ZH' # See available languages: https://www.deepl.com/docs-api/translating-text/
voice = "zh-CN-XiaochenNeural"  # Choose the voice for your selected language: https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support

# -------------------- Default Settings --------------------------------
SOURCE_LANGUAGE = 'EN'
file_address = 'list.csv'  # Input file with English words and phrases 

# Deepl API for translations
HOST = 'https://api-free.deepl.com/v2/translate?'
API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'

# MS API for voice recording
url = "https://microsoft-edge-text-to-speech.p.rapidapi.com/TTS/EdgeTTS"
headers = {
    'x-rapidapi-host': "microsoft-edge-text-to-speech.p.rapidapi.com",
    'x-rapidapi-key': "xxxxxxxxxxxxxxxxxxxxxxxxxx"
}


# -------------------- Get translations --------------------------------
def translate(text):
    response = requests.post(url=HOST,
                             data={
                                 'target_lang': TARGET_LANGUAGE,
                                 'source_lang': SOURCE_LANGUAGE,
                                 'auth_key': API_KEY,
                                 'text': text
                             })

    translation = response.json()["translations"][0]["text"]
    return translation


data = pd.read_csv(file_address)

for index, sentence in data.iterrows():
    text_word = sentence['WORD']
    text_phrase = sentence['PHRASE']
    text_word_translated = translate(text_word)
    text_phrase_translated = translate(text_phrase)
    data.loc[index, 'TRANSLATED_WORD'] = text_word_translated
    data.loc[index, 'TRANSLATED_PHRASE'] = text_phrase_translated

# ------------------Get audios for each sentence and save in the same line----------

for index, sentence in data.iterrows():
    text = sentence['TRANSLATED_PHRASE']
    querystring = {"text": text, "voice_name": voice}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    audio = response.text[16:-2]
    print(audio)
    data.loc[index, 'AUDIO'] = audio


# ------------------CSV File for ANKI APP ----------
anki = pd.DataFrame(data={}, columns=['front', 'back', '1', '2', '3', '4', 'audio'])
for index, sentence in data.iterrows():
    text_word = sentence['WORD']
    text_phrase = sentence['PHRASE']
    text_word_translated = sentence['TRANSLATED_WORD']
    text_phrase_translated = sentence['TRANSLATED_PHRASE']
    audio = sentence['AUDIO'][25:]
    front = f'<i>{text_word}</i><br>{text_phrase}'
    back = f'<i>{text_word_translated}</i><br>{text_phrase_translated}'
    dict = {'front': [front], 'back': [back], '1': '', '2': '', '3': '', '4': '', 'audio': [audio]}
    new_row = pd.DataFrame(dict)
    anki = pd.concat([anki, new_row], ignore_index=True)
anki.to_csv(f'anki_{TARGET_LANGUAGE}.csv', index=False, header=False, encoding="utf-8")
