import os

from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()

apikey = os.getenv('apikey')
url = os.getenv('url')

version = '2022-11-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version= version,
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(englishText):
    frenchText = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    return frenchText


def frenchToEnglish(frenchText):
    englishText = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    return englishText
