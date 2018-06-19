import os
import json
import base64
import urllib3
http = urllib3.PoolManager()
f#rom OmegaExpansion import oledExp

globalBaseUrl     = "https://jsonplaceholder.typicode.com/"
bearerToken = ""

def getAPIData(baseUrl):
    url = baseUrl + 'posts'

    # execute the GET request
    data = http.request(
        'GET',
        url,
    )
    return data

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
def mainProgram(baseUrl):

    # use api to get data
    data= getAPIData(baseUrl)
    if not data:
        print("ERROR: Could not retreive data!")
        exit()

    print('Got data! ', data)
    # display the tweet on the OLED
##    oledWriteData(data['body'])
    print(data)

    print('Done!')


if __name__ == "__main__":
	mainProgram(globalBaseUrl)
