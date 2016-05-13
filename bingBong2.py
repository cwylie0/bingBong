import webbrowser
import time
import random

url = "http://www.bing.com/search?q="
imageUrl = "http://www.bing.com/images/search?q="
nb = raw_input('Enter filename: ')
counter = raw_input('Enter points needed: ')
counting = int(counter) * 2
file = open(nb, 'r')

wordList = []
with open(nb,'r') as f:
    for line in f:
        for word in line.split():
            wordList.append(word)
	     
i = 1
while i <= counting:
        queryTerm = wordList[random.randrange(0, len(wordList))]
	print "Word #%d: %s" % (i, queryTerm)
	webbrowser.open_new_tab(imageUrl+queryTerm)
	time.sleep(3)
	i += 1

file.close()
