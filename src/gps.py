import csv
def inbox(x,y,P):
	if P[0][0] <=x and x<=P[1][0] and P[0][1]<=y and y<=P[1][1]:
		return True
	else:
		return False

def getstate(x,y,boxes):
	for state,box in boxes.iteritems():
		if inbox(x,y,box):
			return state

	return 'none'

def initializeboxes() :
	geocode = {}
	print 'initialising bounding boxes '
	filename="bounding_box.csv"
	with open(filename,'rb') as f :
		csvreader = csv.reader(f, delimiter=',', quotechar='|')
		for row in csvreader:
			fi = (float(row[1]),float(row[2]))
			la = (float(row[3]),float(row[4]))
			geocode[row[0]] = (fi,la)
			# print row
	return geocode

if __name__=='__main__':
	boxes = initializeboxes()
	print getstate(73.123651, 18.990534,boxes)