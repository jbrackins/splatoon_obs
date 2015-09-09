# -*- coding: utf-8 -*-

import os
import subprocess as sub
import urllib2
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser
TWITTERUSER = "splatoonmaps"

def getAll():
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

        lobby = info.split("maps", 1)[0]
        rest = info.split("maps", 1)[1]
        game = rest.split(":",1)[0]
        game = game.replace(game[:2], '')
        mapA = info.split("& ", 1)[0]  
        mapA = mapA.split(": ", 1)[1]  
        mapB = info.split("& ", 1)[1]

        #stripppp
        lobby = lobby.strip()
        game = game.strip()
        mapA = mapA.strip()
        mapB = mapB.strip()
        print "Lobby     :", lobby
        if "Turf" not in lobby: 
            print "Game Mode :", game
        print "Map A     :", mapA
        print "Map B     :", mapB
        print '----------------------------------'

def getRecent():
    # get the most recent tweet from Twitter
    page = urllib2.urlopen("http://twitter.com/" + TWITTERUSER)
    soup = BeautifulSoup(page)

    #print soup#.getText()

    contentTags = soup.findAll('p', attrs={"lang" : "en" })
    twitterTweet = contentTags[0]

    #print contentTags

    sep = '#'

    #For some reason, it's being inconsistent for
    #Turf Wars...
    for i in range(0,1):
        info = contentTags[i].getText()
        info = info.replace("&amp;", "&")
        info = info.split(sep, 1)[0]

        lobby = info.split("maps", 1)[0]
        rest = info.split("maps", 1)[1]
        game = rest.split(":",1)[0]
        game = game.replace(game[:2], '')
        mapA = info.split("& ", 1)[0]  
        mapA = mapA.split(": ", 1)[1]  
        mapB = info.split("& ", 1)[1]

        #stripppp
        lobby = lobby.strip()
        game = game.strip()
        mapA = mapA.strip()
        mapB = mapB.strip()
        #print "Lobby     :", lobby
        #if "Turf" not in lobby: 
        #    print "Game Mode :", game
        #print "Map A     :", mapA
        #print "Map B     :", mapB
        #print '----------------------------------'
    return lobby, game, mapA, mapB

if __name__ == "__main__":
    
    print "ALL"
    getAll()
    print "RECENT"
    getRecent()
