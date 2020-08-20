def filterEntities(nlu_entities, targetEntities):
    textEntities = []
    for entity in nlu_entities:
        if(entity['type'] in targetEntities):
            textEntities.append(entity['text'])
    return textEntities

def highlightText(text, entitiesText):
    for word in entitiesText['translations']:
        text = text.replace(word['translation'],  '<mark style="background-color: LightSkyBlue"> '+ word['translation'] + "</mark>")
    return { 'highlightedText': text }