from twitter import *

access_token = "" #Third Line in text file
access_token_secret = "" #Fourth Line in text file
consumer_key = ""  #First Line in text file
consumer_key_secret = "" #Second Line in text file

#t = Twitter(auth=Oauth(access_token,access_token_secret,consumer_key,consumer_key_secret))


def openFile(filename):
    s = Scanner(filename)
