from nltk.data import load
from nltk.chunk import tree2conlltags
from nltk.tokenize import RegexpTokenizer

regex = r"[A-Z][a-z]+|[a-z]+\'[a-z]+|[a-z]+|[A-Z]+\'[A-Z]+|[A-Z]+"
tokenizer = RegexpTokenizer(regex)

POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
tagger = load(POS_TAGGER)

_BINARY_NE_CHUNKER = 'chunkers/maxent_ne_chunker/english_ace_binary.pickle'
binary_ner = load(_BINARY_NE_CHUNKER) 

def named_entity_recognition(input_text):
    
    tags = tagger.tag(tokenizer.tokenize(input_text)) 
    ne_tree_multiclass = binary_ner.parse(tags)
    iob_tagged_multiclass = tree2conlltags(ne_tree_multiclass)

    structured_elements = [x for x in iob_tagged_multiclass if x[2] is not 'O']
    print(iob_tagged_multiclass)

    return 'xd'


