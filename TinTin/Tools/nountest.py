import nltk
import sys
import time
from tintin import TinTin

lines = str(sys.argv[1])
is_noun = lambda pos: pos[:2] == 'NN'
tokenized = nltk.word_tokenize(lines)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 

for noun in nouns:
  TinTin.showme("<094>--------------------- " + str(noun))
