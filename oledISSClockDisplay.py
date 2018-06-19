import urllib2
import json
import time
from OmegaExpansion import oledExp

if oledExp.driverInit() != 0:
    print('ERROR: Could not initialise the OLED Expansion')
    exit()

oledExp.clear()

currenttime = ""
currentdate = ""
currentlat = ""
currentlon = ""

place = False

while True:
    place = not place
    prevlat = currentlat
    prevlon = currentlon
    prevtime = currenttime
    prevdate = currentdate
    currenttime = time.strftime("%H:%M:%S")
    currentdate = time.strftime("%a, %d/%m/%Y")

    req = urllib2.Request("http://api.open-notify.org/iss-now.json")
    response = urllib2.urlopen(req)

    obj = json.loads(response.read())

    if currenttime != prevtime:
        if not place:
            oledExp.setCursor(0,0)
            oledExp.write(currenttime)

    if currentdate != prevdate:
        if not place:
            oledExp.setCursor(2,0)
            oledExp.write(currentdate)

    currentlat = obj['iss_position']['latitude']
    if currentlat != prevlat:
        if not place:
            oledExp.setCursor(4,0)
            if float(currentlat) < 0:
                oledExp.write(str(currentlat)[1:] + ' S    ')
            else:
                oledExp.write(str(currentlat) + ' N    ')

    currentlon = obj['iss_position']['longitude']
    if currentlon != prevlon:
        if not place:
            oledExp.setCursor(6,0)
            if float(currentlon) < 0:
                oledExp.write(str(currentlon)[1:] + ' W    ')
            else:
                oledExp.write(str(currentlon) + ' E    ')

    if place:
        if currenttime != prevtime:
            mapreq = urllib2.Request("http://nominatim.openstreetmap.org/reverse?format=json&lat=" + obj['iss_position']['latitude'] + "&lon=" + obj['iss_position']['longitude'] + "&zoom=18&addressdetails=1", headers={ 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4' })
            mapresponse = urllib2.urlopen(mapreq)

            mapobj = json.loads(mapresponse.read())

            print(mapobj)
            
##            town = mapobj['hamlet']
##            county = mapobj['county']
##            state = mapobj['state']
##            country = mapobj['country']
##
##            oledExp.clear()
##
##            oledExp.setCursor(0,0)
##            oledExp.write(hamlet)
##
##            oledExp.setCursor(2,0)
##            oledExp.write(county)
##
##            oledExp.setCursor(4,0)
##            oledExp.write(state)
##
##            oledExp.setCursor(6,0)
##            oledExp.write(country)
            
