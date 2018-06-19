import os
import json
import base64
import urllib3
http = urllib3.PoolManager()
from OmegaExpansion import oledExp

baseUrl     = "https://jsonplaceholder.typicode.com/posts"
bearerToken = ""

def getAPIData():
    url = baseUrl + 'posts'

    # execute the GET request
    r = http.request(
        'GET',
        url,
        headers=headers,
        fields=params
    )

def oledWriteTweet(text):
    if oledExp.driverInit() != 0:
        print 'ERROR: Could not initialize the OLED Expansion'
        return False

    # clear the display
    oledExp.clear()


    # set the cursor to the next line
    oledExp.setCursor(0,0)

    # write out the tweet
    oledExp.write(text)



### MAIN PROGRAM ###
def mainProgram():

    # use api to get data
    data= getAPIData()
    if not data:
        print "ERROR: Could not retreive data!"
        exit()

    print 'Got data! ', tweet
    # display the tweet on the OLED
    oledWriteTweet(data['text'])

    print 'Done!'


if __name__ == "__main__":
	mainProgram()
