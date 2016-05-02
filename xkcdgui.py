#!/usr/bin/env python
import sys
k = sys.argv
l = len(k)

import urllib2
import json, urllib
def download(curr, link):
	try:
		urllib.urlretrieve(link,"/tmp/" + str(curr) + ".jpg")
	except Exception,e:
		print("Error downloading image. Please try again later.")
		exit()


def get_link_num(curr):
	try:
		if(curr != 0):
			url = 'http://xkcd.com/' + str(curr) +'/info.0.json'
		else:
			url = 'http://xkcd.com/info.0.json'
		latest = 'http://xkcd.com/info.0.json'
		#print url
		response = urllib2.urlopen(url)
		html = response.read()
		parsed_json=json.loads(html)

		response2 = urllib2.urlopen(latest)
		html2 = response2.read()
		parsed_json2 = json.loads(html2)
		#print(parsed_json['img'])
		link = parsed_json['img']
		num = parsed_json['num']
		latest = parsed_json2['num']
		return link, num, latest
	except urllib2.HTTPError, err:
		if err.code == 404:
			print "Error. Make sure you the comic number is correct and within bounds."
		else:
			print "There was some error. Please try again"
		exit()
		return -1
		

import os.path
def check(i):
	return os.path.isfile('/tmp/' + str(i) + '.jpg')

path = ''
def initialize():
	if(l == 2 and k[1] > 0):
		link, curr, latest = get_link_num(k[1])
	else:
		link, curr, latest = get_link_num(0)
	if(not check(curr)):
		download(curr,link)
	global path
	path = '/tmp/' + str(curr) + '.jpg'
	return link,curr,latest,path


import Tkinter as tk
from PIL import ImageTk, Image
link, curr, latest, path = initialize()
root = tk.Tk()
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")



def callback_next(e):
	global curr, latest
	if(curr < latest):
		global curr
		curr += 1
		if(not check(curr)):
			lst = get_link_num(curr)
			link = lst[0]
			download(curr,link)
		global path
		path = '/tmp/' + str(curr) + '.jpg'
		img2 = ImageTk.PhotoImage(Image.open(path))
		panel.configure(image = img2)
		panel.image = img2

def callback_back(e):
	global curr, latest
	if(curr > 1):
		global curr
		curr -= 1
		if(not check(curr)):
			lst = get_link_num(curr)
			link = lst[0]
			download(curr,link)
		global path
		path = '/tmp/' + str(curr) + '.jpg'
		img2 = ImageTk.PhotoImage(Image.open(path))
		panel.configure(image = img2)
		panel.image = img2

def callback_exit(e):
	root.destroy()


root.bind("<Escape>", callback_exit)
root.bind("<Left>", callback_back)
root.bind("<Right>", callback_next)
root.mainloop()



