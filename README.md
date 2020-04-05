# Firebase-Extractor //Mobile OSINT//

This tool is written in python2, the purpose of this tool is to parse all the results from Bing search.Basically whenever a firebaseio URL is found for an app , User instead of searching for sensitive data by going manually through the search results can use this tool.This tool works by using the given Firebase URL as a search query in the bing search engine, scraping the first 4 pages from the search results , it then finally parses all the URL's for sensitive keywords.


##Screenshot

![Firebase extractor](https://raw.github.com/viperbluff/Firebase-Extractor/blob/master/firebase.png)


Below Modules were Used:

1.sys
2.requests
3.bs4  // pip install bs4 //
4.urllib2
5.pyfiglet // pip install pyfiglet //
6.re 

[+]bs4(Beautiful soup) module is used for parsing and extracting data specific to html.
[+]pyfiglet module is used for generating the banner for the tool.

Running Instructions:

on command line run python firebase.py xyz.firebaseio.com 
where xyz is the app or company specific name.


