from ibm_watson import NaturalLanguageUnderstandingV1, LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions
import os

from dotenv import load_dotenv
load_dotenv()

def translate(text, model):
    authenticator = IAMAuthenticator(os.getenv('APIKEY_Translator'))
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url('https://gateway.watsonplatform.net/language-translator/api')

    translation = language_translator.translate(
        text=text,
        model_id=model).get_result()
    return translation

def getEntities(text):
    authenticator = IAMAuthenticator(os.getenv('APIKEY_NLU'))
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2019-11-16',
        authenticator=authenticator)
    natural_language_understanding.set_service_url('https://gateway.watsonplatform.net/natural-language-understanding/api')

    response = natural_language_understanding.analyze(
        text=text,
        features=Features(
        entities=EntitiesOptions())).get_result()
    return response['entities']