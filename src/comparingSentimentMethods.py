#!/usr/bin/env python
import re
import nltk
import os
import sys
import codecs
import json
import csv
from nltk.corpus import wordnet as wn


def bingReadWords(filename):
	words=[]
	with open(filename) as f:
		for line in f:
			words.append(str(line))
	return set(words)

def bingCalculateSentiment(listOfTokens,bingPositiveWords,bingNegativeWords):
	score=0.0
	for token in listOfTokens:
		print token,
		if token in bingNegativeWords:
			print "-1",
			score-=-1.0
		elif token in bingPositiveWords:
			print "1",
			score+=1
		print ""
	if score>0:
		return 1
	elif score==0:
		return 0
	else:
		return -1

def affinReadwords(filename):
	dic={}
	with open(filename) as f:
		for line in f:
			word,score=line.split('\t')
			score=int(score)
			dic[word]=score
	return dic

def affinCalculateSentiment(listOfTokens,affinDictionary):
	score=0.0
	for token in listOfTokens:
		if affinDictionary.has_key(token):
			score+=affinDictionary[token]

	if score>0:
		return 1
	elif score==0:
		return 0
	else:
		return -1

def sentiReadWord(filename):
	dic={}
	lines = codecs.open(filename, "r", "utf8").read().splitlines()
	lines = filter((lambda x : not re.search(r"^\s*#", x)), lines)
	for i, line in enumerate(lines):
		fields = re.split(r"\t+", line)
		fields = map(unicode.strip, fields)
		pos, offset, pos_score, neg_score, synset_terms, gloss = fields
		if pos and offset:
			offset = int(offset)
			dic[(pos,offset)] = (float(pos_score), float(neg_score))
	return dic

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wn.ADJ
    elif treebank_tag.startswith('V'):
        return wn.VERB
    elif treebank_tag.startswith('N'):
        return wn.NOUN
    elif treebank_tag.startswith('R'):
        return wn.ADV
    else:
        return ''

def sentiCalculateSentiment(listOfTokens,sentiDictionary):
	score=0
	listOfTokens = nltk.pos_tag(listOfTokens)
	print listOfTokens
	print "here"
	for token in listOfTokens:
		negScore=0
		posScore=0
		tag=get_wordnet_pos(token[1])
		synset_list = wn.synsets(token[0],tag)
		for synset in synset_list:
			pos = synset.pos
			offset = synset.offset
			if (pos, offset) in sentiDictionary:
				pos_score, neg_score = sentiDictionary[(pos, offset)]
				if pos_score>neg_score:
					posScore+=1
				elif neg_score>pos_score:
					negScore+=1
		if negScore>posScore:
			score= score-1
		elif negScore<posScore:
			score+=1
	if score>0:
		return (score,1)
	elif score==0:
		return (score,0)
	else:
		return (score,-1)

def main():
	print 'nothing'	

if __name__=='__main__':
	main()