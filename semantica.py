from nltk.wsd import lesk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import wordnet as wn 
from nltk.data import load
from nltk.corpus import stopwords

import re
import random

regex = r"\w+\'\w+|\w+"
tokenizer = RegexpTokenizer(regex)
eng_stopwords = set(stopwords.words('english'))
regexes_dict = {'N\w{1,3}':'nombres', 'J\w{1,2}':'adjetivos', 'V\w{1,2}':'verbos', 'RB?':'adverbios'}


POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
tagger = load(POS_TAGGER)


def antonimos(input_text):
    sentences = sent_tokenize(input_text)

    regex = r'J\w{1,2}'

    for sentence in sentences:

        tokenized_text = tokenizer.tokenize(sentence)
        tags = tagger.tag(tokenized_text)

        for tag in tags:
            tag_category = tag[1] 

            match = re.match(regex, tag_category)
            if(match):
                antonyms = []
                lemmas = wn.synset(lesk(sentence, tag[0]).name()).lemmas()
                for lemma in lemmas:
                    if(lemma.antonyms()):
                        for antonym in lemma.antonyms():
                            antonyms.append(antonym)

                if len(antonyms) > 0:
                    rand_ant = random.choice(antonyms).name()
                    replace_text = '<span style="color:red"> _'+ tag[0] +'_ </span> <span style="color:blue"> **'+rand_ant+'** </span>'
                    input_text = input_text.replace(" "+tag[0]+" ", replace_text, 1)

    return input_text

def sinonimos(input_text):
    sentences = sent_tokenize(input_text)

    regex = r'J\w{1,2}'

    for sentence in sentences:

        tokenized_text = tokenizer.tokenize(sentence)
        tags = tagger.tag(tokenized_text)

        for tag in tags:
            tag_category = tag[1] 

            match = re.match(regex, tag_category)
            if(match):
                synset = lesk(sentence, tag[0])
                if synset:
                    synonyms = synset.lemma_names()
                    rand_syn = random.choice(synonyms)
                    if rand_syn != tag[0]:
                        replace_text = '<span style="color:red"> _'+ tag[0] +'_ </span> <span style="color:blue"> **'+rand_syn+'** </span>'
                        input_text = input_text.replace(" "+tag[0]+" ", replace_text, 1)

    return input_text


def desambiguar(input_text):
    sentences = sent_tokenize(input_text)

    synsets_dict= dict()
    for sentence in sentences:
        tokens = tokenizer.tokenize(sentence)
        
        for token in tokens:
            if token.lower() not in eng_stopwords:
                synset = lesk(sentence, token)
                if synset:
                    synsets_dict[token] = synset

    return synsets_dict

