import spacy
from nltk.data import load
from nltk.chunk import tree2conlltags
from nltk.tokenize import RegexpTokenizer

import re

regex = r"[A-Z][a-z]+|[a-z]+\'[a-z]+|[a-z]+|[A-Z]+\'[A-Z]+|[A-Z]+"
tokenizer = RegexpTokenizer(regex)

nlp = spacy.load("en_core_web_sm")

def named_entity_recognition(input_text):
    
    doc = nlp(input_text)
    labels = [x.label_ for x in doc.ents]

    render = spacy.displacy.render(doc, style='ent')

    render = re.sub(r"line-height: \d.\d|line-height: \d", "line-height: 2.5", render) #line spacing is not consistent in the original render

    return render


