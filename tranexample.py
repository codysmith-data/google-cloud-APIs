# -*- coding: utf-8 -*-

from google.cloud import translate_v2 as translate

#Creating function to translate text to English
def translate_text(text, target='en'):

        #Creating instance of translate client
        client = translate.Client()

        #Translating
        result = client.translate(text, target_language=target)

        #Printing results
        print('Text:', result['input'])
        print('Translation:', result['translatedText'])
        print('Detected source lang:', result['detectedSourceLanguage'])

#Example text to translate
example_text = 'Me gustaria una cerveza.'

#Using translating function
translate_text(example_text)