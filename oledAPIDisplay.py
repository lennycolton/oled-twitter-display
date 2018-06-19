import os
import json
import base64
import urllib3
http = urllib3.PoolManager()
from OmegaExpansion import oledExp

baseUrl     = "https://jsonplaceholder.typicode.com/"
bearerToken = ""

def getAPIData():
    url = baseUrl + 'posts'

    # execute the GET request
    req = urllib3.Request(url)
    response = urllib2.urlopen(req)
    return response

##def oledWriteData(text):
##    if oledExp.driverInit() != 0:
##        print 'ERROR: Could not initialize the OLED Expansion'
##        return False
##
##    # clear the display
##    oledExp.clear()
##
##
##    # set the cursor to the next line
##    oledExp.setCursor(0,0)
##
##    # write out the tweet
##    oledExp.write(text)



### MAIN PROGRAM ###
def mainProgram():

    # use api to get data
    data= getAPIData()
    if not data:
        print("ERROR: Could not retreive data!")
        exit()

    print('Got data! ', data)

    obj = json.loads(response.read())
    # display the tweet on the OLED
##    oledWriteData(data['body'])
    print(obj['body'])

    print('Done!')


if __name__ == "__main__":
	mainProgram()
