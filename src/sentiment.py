import json
from load_sentiment import *

def load_tweet(tweet_file):
	dictionary = load_sentiments('ANEW.csv')
	data = []
	# print "yaya"
	with open(tweet_file) as f:
		for line in f:
			try:
				data.append(json.loads(line))
			except:
				pass

		for i in range(len(data)):
			calculate_sentiment(data[i],dictionary)

def probability(deviation):
	return 1/float(deviation)

def calculate_sentiment(tweet,dictionary,kind):
	# print dictionary.keys()
	# tweet = json.loads(data)
	# print tweet['text'].encode('utf-8')
	print 'Im herer '
	if (tweet['text']!=None):
		text = tweet['text'].encode('utf-8')
		# print tweet['text']	
		line = text.split(' ')
		sc_valence = float(0)
		den = float(0)
		flag=False
		for word in line:
			if word in dictionary:
				flag = True
				values = dictionary[word]
				sc_valence += float(values[kind][0])*probability(values[kind][1])
				den +=probability(values[kind][1])
		print 'score calculated'
		if(flag):
			# print("Y!, %s -> %f\n" % (text,sc_valence/den))
			return sc_valence/den
		else:
			# print("N!, %s -> %f\n" % (text,sc_valence))
			return sc_valence