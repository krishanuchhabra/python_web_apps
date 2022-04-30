#!/usr/bin/env python

from bs4 import BeautifulSoup

import urllib

html =urllib.urlopen("http://www.securitytube.net/video/3000")

print html.code
#gives200

bt = BeautifulSoup(html.read(), "lxml")

#forcing it to use lxml parser as its html parset is very bad

#to find title

print bt.title

print bt.title.string
#prints the string bw the title tags

print bt.meta
#prints 1st meta tag

print bt.meta
#prints the 2nd meta tag

#to print all meta tags in the documents
allMetaTags = bt.find_all('meta')

print allMetaTags[0]
#returns the first meta tag in the allMetaTag list


print allMetaTags[0]['content']


#find all can also take regex, css,etc

#find all a tags and print href value
allLinks = bt.find_all('a')

print len(allLinks)

for links in allLinks:
    print links['href']


#find all the text in html

print bt.get_text()


