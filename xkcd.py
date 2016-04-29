#!/usr/bin/env python2


import sys
k = sys.argv
l = len(k)
arg = "/"
if(l == 2):
	arg = arg + str(k[1]) + '/'



import urllib2
url = 'http://xkcd.com' + arg + 'info.0.json'
print url
response = urllib2.urlopen(url)
html = response.read()
#print html


import json
parsed_json=json.loads(html)
#print(parsed_json['img'])
link=parsed_json['img']



import urllib
urllib.urlretrieve(link,"/tmp/File.jpg")



from PIL import Image
image = Image.open('/tmp/File.jpg')
image.show()