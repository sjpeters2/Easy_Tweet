from twitter import *
from scanner import *

access_token = "" #Third Line in text file
access_token_secret = "" #Fourth Line in text file
consumer_key = ""  #First Line in text file
consumer_key_secret = "" #Second Line in text file

#t = Twitter(auth=Oauth(access_token,access_token_secret,consumer_key,consumer_key_secret))


def readFile(filename):
    fp = open(filename,"r")
	
	consumer_key = fp.readline()
	consumer_key_secret = fp.readline()
	access_token = fp.readline()
	access_token_secret = fp.readline()
	
	fp.close()

	
