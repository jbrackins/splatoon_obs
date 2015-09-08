import os
import subprocess as sub
import urllib2
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser
TWITTERUSER = "splatoonmaps"


# get the most recent tweet from Twitter
page = urllib2.urlopen("http://twitter.com/" + TWITTERUSER)
soup = BeautifulSoup(page)

#print soup#.getText()

contentTags = soup.findAll('p', attrs={"lang" : "en" })
twitterTweet = contentTags[0]

#print contentTags

sep = '#'


for i in contentTags:
    info = i.getText()
    info = info.replace("&amp;", "&")
    info = info.split(sep, 1)[0]
    print info
