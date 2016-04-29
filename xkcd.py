#!/usr/bin/env python


import sys
k = sys.argv
l = len(k)
arg = "/"
if(l == 2):
	arg = arg + str(k[1]) + '/'



import urllib2
try: 
	url = 'http://xkcd.com' + arg + 'info.0.json'
	#print url
	response = urllib2.urlopen(url)
	html = response.read()
except urllib2.HTTPError, err:
	if err.code == 404:
		print "Error. Make sure you the comic number is correct and within bounds."
	else:
		print "There was some error. Please try again"
	exit()
#print html


import json
parsed_json=json.loads(html)
#print(parsed_json['img'])
link=parsed_json['img']



import urllib
try:
	urllib.urlretrieve(link,"/tmp/File.jpg")
except Exception,e:
	print("Error downloading image. Please try again later.")
	exit()


from PIL import Image
image = Image.open('/tmp/File.jpg')
image.show()
