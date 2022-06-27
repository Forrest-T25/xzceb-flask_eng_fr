import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')

def englishToFrench(englishText):
    """Function for translating English to French"""
    FrenchText =language_translator.translate(
        text=englishText,
        model_id='en-fr'
        ).get_result()
    FrenchText = FrenchText['translation'][0]['translation']
    return FrenchText

def frenchToEnglish(frenchText):
    """ Function for translating French to English"""
    EnglishText = language_translator.translate(
        text = frenchText,
        model_id='fr-en'
        ).get_result()
    EnglishText =EnglishText['translation'][0]['translation']
    return EnglishText
