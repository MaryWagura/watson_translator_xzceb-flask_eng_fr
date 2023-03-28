import unittest
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#import englishToFrench, frenchToEnglish
import os
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['vPwok2dhCfRSaJJIkQdvljkhfIG_qXxomL2DHwkZ12z8']
url = os.environ['https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/75bb803f-318d-400f-8200-574454df1671']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

class TestTranslator(unittest.TestCase):
     def test_englishToFrench(self):
        # Test the English to French translation function
        english_text = "Hello"
        french_text = self(english_text)
        expected_text = "Bonjour"
        self.assertEqual(french_text, expected_text)
     def test_frenchToEnglish(self):
        # Test the French to English translation function
        french_text = "Bonjour"
        english_text = self(french_text)
        expected_text = "Hello"
        self.assertEqual(english_text, expected_text)

if __name__ == '__main__':
     unittest.main()
