from nltk.wsd import lesk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import wordnet as wn 

regex = r"\w+\'\w+|\w+"
tokenizer = RegexpTokenizer(regex)

def desambiguar(input_text):
    sentences = sent_tokenize(input_text)

    synsets_dict= dict()
    for sentence in sentences:
        tokens = tokenizer.tokenize(sentence)
        
        for token in tokens:
            synset = lesk(sentence, token)
            if synset:
                synsets_dict[token] = synset

    return synsets_dict