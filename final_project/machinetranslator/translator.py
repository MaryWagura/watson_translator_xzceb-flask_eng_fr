#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['vPwok2dhCfRSaJJIkQdvljkhfIG_qXxomL2DHwkZ12z8']
url = os.environ['https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/75bb803f-318d-400f-8200-574454df1671']


    # Set up authentication
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-09-01',
    authenticator=authenticator
)

# Set the service URL
language_translator.set_service_url(url)

def english_to_french(english_text):
   # Call the Watson Language Translator API to translate English to French
    translation = language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()

    # Extract the translated text from the API response
    french_text = translation['translations'][0]['translation']

    return french_text

    # def french_to_english(french_text):
    # # Call the Watson Language Translator API to translate French to English
    #     translation = language_translator.translate(
    #     text=french_text,
    #     source='fr',
    #     target='en'
    # ).get_result()

    # Extract the translated text from the API response
    english_text = translation['translations'][0]['translation']
    return english_text
