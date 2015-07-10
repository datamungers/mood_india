# from sentiment import *
# from load_sentiment import *
from twitterstream import *
import csv
from normalize import *
from comparingSentimentMethods import *

scoreOfStates={}
geocode = {}
# Work - Figure out how to have the data structure to support past 24 hours and whole database results
def checkLiesInIndia(TweetInfo) :
	if TweetInfo.has_key("place"):
			if TweetInfo["place"].has_key("country_code"):
				# if TweetInfo["place"]["country_code"] == "IN":
				return True
	return False

def writeTweetData(TweetInfo):  # Figure out the best way to store the data as we procure it
	filename="tweetData.csv"
	with open(filename,'a') as csv_file :
		writer = csv.writer(csv_file,delimiter=',')
		listOfitems=[]
		if TweetInfo.has_key("text"):
			listOfitems.append(str(TweetInfo["text"]))
		else :
			listOfitems.append("")

def writeTweetData(TweetInfo):  # Figure out the best way to store the data as we procure it
	filename="tweetData.csv"
	with open(filename,'a') as csv_file :
		writer = csv.writer(csv_file,delimiter=', ')
		listOfitems=[]
		if TweetInfo.has_key("text"):
			text = TweetInfo['text']
			text = str(text)
			for i in range(len(text)):
				if text[i]=='\n' or text[i] =='\r':
					text[i] ='^'
			listOfitems.append(str(text))
		else :
			listOfitems.append("")
		if TweetInfo.has_key('retweet_count'):
			listOfitems.append(str(TweetInfo['retweet_count']))
		else:
			listOfitems.append("")

		if TweetInfo.has_key('user'):
			if TweetInfo['user'].has_key('id'):
				listOfitems.append(str(TweetInfo['user']['id']))
			else:
				listOfitems.append("")

			if 	TweetInfo['user'].has_key('followers_count'):
				listOfitems.append(str(TweetInfo['user']['followers_count']))
			else:
				listOfitems.append("")

			if 	TweetInfo['user'].has_key('statuses_count'):
				listOfitems.append(str(TweetInfo['user']['statuses_count']))
			else:
				listOfitems.append("")
		else:
			listOfitems.append("")
			listOfitems.append("")
			listOfitems.append("")

		if TweetInfo.has_key("coordinates"):
			listOfitems.append(str(TweetInfo['coordinates']['coordinates'][0]))
			listOfitems.append(str(TweetInfo['coordinates']['coordinates'][1]))
		else:
			listOfitems.append("")
			listOfitems.append("")

		if TweetInfo.has_key("place"):
			if TweetInfo['place'].has_key('full_name'):
				listOfitems.append(str(TweetInfo['place']['full_name']))
			else:
				listOfitems.append("")
			if TweetInfo['place'].has_key('country'):
				listOfitems.append(str(TweetInfo['place']['country']))
			else:
				listOfitems.append("")
			if TweetInfo['place'].has_key('place_type'):
				listOfitems.append(str(TweetInfo['place']['place_type']))
			else:
				listOfitems.append("")
			if TweetInfo['place'].has_key('country_code'):
				listOfitems.append(str(TweetInfo['place']['country_code']))
			else:
				listOfitems.append("")
		else:
			listOfitems.append("")
			listOfitems.append("")
			listOfitems.append("")
			listOfitems.append("")
		writer.writerow(listOfitems)

def inbox(x,y,P):
	if P[0][0] <=x and x<=P[1][0] and P[0][1]<=y and y<=P[1][1]:
		return True
	else:
		return False

def findstate(x,y):
	global geocode
	for state,box in geocode.iteritems():
		if inbox(x,y,box):
			return state
	return 'none'

def addTweetScore(TweetInfo,tweetScore):
	global geocode
	global scoreOfStates
	print "Im here !!!"
	if TweetInfo.has_key("coordinates"):
		if TweetInfo["coordinates"].has_key("coordinates"):
			print "Im here"
			tweetCoords=TweetInfo["coordinates"]["coordinates"]
			print tweetCoords
			res = findstate(float(tweetCoords[0]),float(tweetCoords[1]))
			stateName=str(res)
			print res + " " + stateName + " "
			print ""
			if scoreOfStates.has_key(stateName):
				scoreOfStates[stateName]=((scoreOfStates[stateName][0]+tweetScore),scoreOfStates[stateName][1]+1)
		else:
			print "Coordinates not found"
	else:
		print "coordinates not found"

def initializeScoreDictionary():
	global scoreOfStates
	lines = [line.strip() for line in open('statesNames.txt')]
	for line in lines:
		indexi=5
		stateName=line[0:5]
		scoreOfStates[stateName]=(0,0)

def initializeGeoCode() :
	global geocode
	filename="bounding_box.csv"
	with open(filename,'rb') as f :
		csvreader = csv.reader(f, delimiter=',', quotechar='|')
		for row in csvreader:
			fi = (float(row[1]),float(row[2]))
			la = (float(row[3]),float(row[4]))
			geocode[row[0]] = (fi,la)
			# print row
	# print geocode

def main():
	global scoreOfStates
	initializeScoreDictionary()
	# sentiDictionary=sentiReadWord('SentiWordNet_3.0.0_20100705.txt')
	# bingNegativeWords=bingReadWords('negative-words.txt')
	# bingPositiveWords=bingReadWords('positive-words.txt')
	# print bingPositiveWords
	affinDictionary = affinReadwords('AFINN-111.txt')
	i = 0
	initializeGeoCode()
	print scoreOfStates
	with open("twits.txt") as f:
		for line in f:
			if i == 20:
				break
			# print line
			try:
				TweetInfo = json.loads(line)
				if checkLiesInIndia(TweetInfo) & TweetInfo.has_key('text'):
					i+=1
					listOfTokens= normalize(TweetInfo['text'])
					print listOfTokens
					print ""
					tweetScore = affinCalculateSentiment(listOfTokens,affinDictionary)
					print tweetScore 
					print type(tweetScore)
					print ""
					addTweetScore(TweetInfo,tweetScore)
					print scoreOfStates
					print "done"	
			except:
				print "Exception found"
				pass

	print scoreOfStates

if __name__ == '__main__':
	main()
