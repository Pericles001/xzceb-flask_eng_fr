"""
Module created for translations between English and French
"""
import json
import os

from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()

apikey = os.getenv('apikey')
url = os.getenv('url')

VERSION = '2022-11-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    Method that takes input in english and translates it to french
    :param english_text:
    :return:
    """
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = json.dumps(french_text, indent=2, ensure_ascii=False)
    return french_text


def french_to_english(french_text):
    """
    Method that takes input in French and translates it to english
    :param french_text:
    :return:
    """
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = json.dumps(english_text, indent=2, ensure_ascii=False)
    return english_text
