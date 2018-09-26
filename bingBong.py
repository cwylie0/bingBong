import webbrowser
import time
import random
import string


url = "http://www.bing.com/search?q="
imageUrl = "http://www.bing.com/images/search?q="
exclude = set(string.punctuation)

nb = input('Enter filename: ')
counter = input('Enter points needed: ')
counting = (int(counter)  / 10) * 2
file = open(nb, 'r')

wordList = []
with open(nb,'r') as f:
    for line in f:
        for word in line.split():
            wordList.append(word)
	     
i = 1
while i <= counting:
        queryTerm = wordList[random.randrange(0, len(wordList))]
        while len(queryTerm) < 5:
            queryTerm = wordList[random.randrange(0, len(wordList))]
        
        for c in string.punctuation:
            queryTerm=queryTerm.replace(c,"")
        print ("Word #%d: %s" % (i, queryTerm))
        webbrowser.open_new_tab(imageUrl+queryTerm)
        time.sleep(1)
        i += 1

file.close()