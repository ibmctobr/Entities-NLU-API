from flask import Flask, request
from flask_cors import CORS
from controllers import ibm_services, text_analysis
import os

app = Flask(__name__)
CORS(app)
cf_port = os.getenv('PORT')

@app.route('/', methods=['POST'])
def analyze():
    inputText = request.get_json(force=True)['text']
    languageModel = request.get_json(force=True)['language_model'].split('-')
    chosenEntities = request.get_json(force=True)['entity_types'].split('|')

    try:
        translatedText = ibm_services.translate(inputText, languageModel[0] + '-' + languageModel[1])['translations'][0]['translation']
        nlu_entities = ibm_services.getEntities(translatedText)
        filteredEntities = text_analysis.filterEntities(nlu_entities, chosenEntities)
        
        if(len(filteredEntities) > 0):
            translatedEntities = ibm_services.translate(filteredEntities, languageModel[1] + '-' + languageModel[0])
            response = text_analysis.highlightText(inputText, translatedEntities)
        
        return response
    except:
        return { 'highlightedText': 'Not enough text to translate. Try again.' }

if __name__ == '__main__':
    if cf_port is None:
        app.run(host='0.0.0.0', port=5000, debug=False)
    else:
        app.run(host='0.0.0.0', port=int(cf_port), debug=False)