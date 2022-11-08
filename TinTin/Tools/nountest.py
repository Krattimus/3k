import nltk
import sys
import time
from tintin import TinTin

lines = str(sys.argv[1])
is_noun = lambda pos: pos[:2] == 'NN'
tokenized = nltk.word_tokenize(lines)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 

seconds = 0.1
delay = 1
for noun in nouns:
  TinTin.delay("delay" + str(delay), "#showme <094>--------------------- " + str(noun), seconds)
  delay = delay + 1
  TinTin.delay("delay" + str(delay), "#send look at " + str(noun), seconds)
  delay = delay + 1
  TinTin.delay("delay" + str(delay), "#send search " + str(noun), seconds)
  seconds = seconds + 2
  delay = delay + 1
