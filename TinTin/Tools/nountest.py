import nltk
import sys

print ("#showme <094>------------------------------------- ")
#print ("#showme " + str(sys.argv[1]))

lines = str(sys.argv[1])
# function to test if something is a noun
is_noun = lambda pos: pos[:2] == 'NN'
# do the nlp stuff
tokenized = nltk.word_tokenize(lines)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 

#print ("#showme <094>" + str(nouns))
for noun in nouns:
  print ("#showme <094>" + str(noun))

print ("#showme <094>------------------------------------- ")
