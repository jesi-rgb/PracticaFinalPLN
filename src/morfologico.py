import spacy
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter

regex = r"[A-Z][a-z]+|[a-z]+\'[a-z]+|[a-z]+|[A-Z]+\'[A-Z]+|[A-Z]+"
tokenizer = RegexpTokenizer(regex)
nlp = spacy.load("en_core_web_sm")
eng_stopwords = set(stopwords.words('english'))

def morph_analysis(input_text):
    sentences = sent_tokenize(input_text)
    
    num_sentences = len(sentences)

    token_list = []
    stops_list = []

    for sentence in sentences:
        tokens = tokenizer.tokenize(sentence)

        for token in tokens:
            if token.lower() in eng_stopwords:
                stops_list.append(token)
            else:
                token_list.append(token)

    num_tokens = len(token_list)
    num_unique_tokens = len(set(token_list))
    num_stops = len(stops_list)
    num_unique_stops = len(set(stops_list))

    top5_tokens = dict(Counter(token_list).most_common(5))

    doc = nlp(input_text)
    nouns_list = len([chunk.text for chunk in doc.noun_chunks])
    adjs_list = len([token.text for token in doc if token.pos_ == "ADJ"])
    advs_list = len([token.text for token in doc if token.pos_ == "ADV"])
    verb_list = len([token.text for token in doc if token.pos_ == "VERB"])


    return (num_sentences, {"Tokens":num_tokens, "Tokens únicos":num_unique_tokens, 
    "Palabras vacías":num_stops, "Palabras vacías únicas":num_unique_stops}, top5_tokens,
    {"Nombres":nouns_list, "Adjetivos":adjs_list, "Adverbios":advs_list, "Verbos":verb_list})







