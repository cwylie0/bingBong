import webbrowser
import time

url = "http://www.bing.com/search?q="
imageUrl = "http://www.bing.com/images/search?q="
nb = raw_input('Enter search terms: ')
for i, word in enumerate(nb.split()):
	print "Word #%d: %s" % (i, word)
	webbrowser.open_new_tab(imageUrl+word)
	time.sleep(5)
