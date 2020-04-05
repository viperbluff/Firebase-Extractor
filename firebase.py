#!/usr/share/python

import urllib,urllib2
from requests import get
import sys
import pyfiglet
from bs4 import BeautifulSoup
import re

def scrap_engine(y):
	c=0

	while c<4: 
		url="https://www.bing.com/search?q=site:%s&go=Search&first=%d1" %(y,c) 
		getRequest=urllib2.Request(url, None, {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}) 
		res=urllib2.urlopen(getRequest)
		parse=BeautifulSoup(res,'html.parser')
		container=parse.find_all('li',class_="b_algo")
		for values in container:
			url=values.a.get('href')
			print "Interesting URL found:\n[+]%s\n" %(url)
			fetch_firebase_data(url)
		c=c+1
	
def fetch_firebase_data(data): 
	json_data=get(data)
	if json_data.status_code == 500:
		keywords=['token','id','password','api-key','url','email','username','number','userid']
		for i in keywords:
			result_match=re.search(i,json_data.text)
			if result_match:
				print "[-]Keyword Identified:%s\n" %(result_match.group())
			else:
				continue
	else:
		print "[-]Site not reachable\n"


def main():
		if len(sys.argv)<2:
			print "Usage:: python firebase.py FirebaseURL\n[*]You can run the tool directly if u don't have FirebaseURL  ::"
			banner=pyfiglet.figlet_format("Firebase Extractor")
			print banner
		else:
			banner=pyfiglet.figlet_format("Firebase Extractor")
			print "%s\n" %(banner)
			URL_to_parse=sys.argv[1]
			print "[*]Parsing Search Engines\n"
			scrap_engine(URL_to_parse)



if __name__=="__main__":
	main()



