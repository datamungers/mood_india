from normalize import *
import csv
from comparingSentimentMethods import *
import matplotlib.pyplot as plt
import numpy as np

listOfTweets = []
annotation = []

def check(emotion):
	if emotion == 'neutral':
		return 0
	elif emotion == 'positive':
		return 1
	else:
		return -1

def read_csv(filename):
	with open(filename,'rb') as csvfile:
		read = csv.reader(csvfile,delimiter='\t')
		for row in read:
			listOfTweets.append(row[3])
			annotation.append(check(row[2]))

def score(given,trueScore):
	if given==-1 and trueScore==0:
		return 1
	elif given==1 and trueScore==0:
		return 1
	else:
		return 0

def tester(listOfTweets,annotation):
	bingNegativeWords=bingReadWords('negative-words.txt')
	bingPositiveWords=bingReadWords('positive-words.txt')
	affinDictionary=affinReadwords('AFINN-111.txt')
	sentiDictionary=sentiReadWord('SentiWordNet_3.0.0_20100705.txt')
	correctCount1=0
	correctCount2=0
	correctCount3=0
	totalNumberOfTweets= len(listOfTweets)
	for i in range(len(listOfTweets)):
		listOfTokens=normalize(listOfTweets[i])
		classified1=bingCalculateSentiment(listOfTokens,bingPositiveWords,bingNegativeWords)
		classified2=affinCalculateSentiment(listOfTokens,affinDictionary)
		sentiback = sentiCalculateSentiment(listOfTokens,sentiDictionary)
		classified3= sentiback[1]
		if classified1!=annotation[i]:
			correctCount1+=1
		if classified2!=annotation[i]:
			correctCount2+=1
		if classified3!=annotation[i]:
			correctCount3+=1

	print "accuracyBing : "+ str(float(correctCount1)/totalNumberOfTweets)+" accuracyAffin : "+ str(float(correctCount2)/totalNumberOfTweets)+" accuracySenti : "+ str(float(correctCount3)/totalNumberOfTweets)

def plothist():

	n_groups = 3

	means_men = (42.3113658071, 39.7803247373, 67.335243553)
	std_men = (1, 2, 3)

	fig, ax = plt.subplots()

	index = np.array([0.5,1.5,2.5])
	bar_width = 0.4

	opacity = 0.4
	error_config = {'ecolor': '0'}

	rects1 = plt.bar(index, means_men, bar_width,
	                 alpha=opacity,
	                 color='b',
	                 error_kw=error_config)

	plt.xlabel('Approach')
	plt.ylabel('Accuracy')
	plt.axis((0,3.4,0,100))
	plt.title('Evaluation')
	plt.xticks(index + bar_width/2, ('Bing Liu', 'AFINN', 'SentiWordNet'))
	plt.legend()

	plt.tight_layout()
	# plt.show()
	plt.savefig('foo.png')

def main():
	# read_csv("sms-test-gold-B.tsv")
	# tester(listOfTweets,annotation)
	plothist()
if __name__=='__main__':
	main()
	