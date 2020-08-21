# Voice Anamnesis API
Using IBM Watson Language Translator and Watson Natural Language Understanding (NLU), highlight words from any text based on the specified entity types.

## Technologies
- Flask
- Watson Language Translator
- Watson Natural Language Understanding

## Prerequisites
- Python version: 3.+

## Run locally (tested for Python 3.7.5)
1. Clone the repo
```
$ git clone https://github.com/ibmctobr/voice-anamnesis-api.git
$ cd voice-anamnesis-api
```

2. Install the packages
```
$ pip install -r requirements.txt
```

3. Create the .env file
```
$ cp .env.example .env
```

4. In the .env file, add the credentials from the Watson Language Translator and NLU services
```
APIKEY_Translator=ENTER-LANGUAGETRANSLATOR-APIKEY-HERE
APIKEY_NLU=ENTER-NLU-APIKEY-HERE
```

5. Run
```
$ python app.py
```

## IBM Cloud Docs
- [List of entity types](https://cloud.ibm.com/docs/services/natural-language-understanding?topic=natural-language-understanding-entity-types-version-1&locale=en-us)
- [List of identifiable languages](https://cloud.ibm.com/docs/services/language-translator?topic=language-translator-identifiable-languages&locale=en-us)

## POST data
```
{
  text: YOUR_TEXT_HERE,
  language_model: LANGUAGE_CODE-en,
  entity_types: ENTITY1|ENTITY2|...
}
```

## Response data
```
{
  highlightedText: HIGHLIGHTED_TEXT_OUTPUT
}
```

## Example
### POST data
```
{
  text: "Eu estou com febre, tosse e dor de cabeça.",
  language_model: "pt-en",
  entity_types: "HealthCondition|Drug|Anatomy"
}
```
### Response data
```
{
  highlightedText: "Eu estou com <mark style=\"background-color: Tomato\"> febre</mark>, <mark style=\"background-color: Tomato\"> tosse</mark> e <mark style=\"background-color: Tomato\"> dor de cabeça</mark>."
}
```
