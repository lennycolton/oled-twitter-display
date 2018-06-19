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
count = 0

while True:
    prevlat = currentlat
    prevlon = currentlon
    prevtime = currenttime
    prevdate = currentdate
    currenttime = time.strftime("%H:%M:%S")
    currentdate = time.strftime("%a, %d/%m/%Y")

    req = urllib2.Request("http://api.open-notify.org/iss-now.json")
    response = urllib2.urlopen(req)

    obj = json.loads(response.read())

    if count != 5:
        oledExp.setCursor(0,0)
        oledExp.write(currenttime)
        if prevtime != currenttime:
            count = count + 1

    if count != 5:
        oledExp.setCursor(2,0)
        oledExp.write(currentdate)

    currentlat = obj['iss_position']['latitude']
    if currentlat != prevlat and count != 5:
        oledExp.setCursor(4,0)
        if float(currentlat) < 0:
            oledExp.write(str(currentlat)[1:] + ' S            ')
        else:
            oledExp.write(str(currentlat) + ' N            ')

    currentlon = obj['iss_position']['longitude']
    if currentlon != prevlon and count != 5:
        oledExp.setCursor(6,0)
        if float(currentlon) < 0:
            oledExp.write(str(currentlon)[1:] + ' W            ')
        else:
            oledExp.write(str(currentlon) + ' E            ')

    if count == 5:
        if currenttime != prevtime:
            mapreq = urllib2.Request("http://nominatim.openstreetmap.org/reverse?format=json&lat=" + obj['iss_position']['latitude'] + "&lon=" + obj['iss_position']['longitude'] + "&zoom=18&addressdetails=1", headers={ 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4' })
            mapresponse = urllib2.urlopen(mapreq)

            mapobj = json.loads(mapresponse.read())

            print(mapobj)

            try:
                town = unicode(mapobj['address']['city'])
            except KeyError:
                try:
                    town = unicode(mapobj['address']['town'])
                except KeyError:
                    try:
                        town = unicode(mapobj['address']['village'])
                    except KeyError:
                        try:
                            town = unicode(mapobj['address']['hamlet'])
                        except KeyError:
                            try:
                                town = unicode(mapobj['address']['water'])
                            except KeyError:
                                try:
                                    town = unicode(mapobj['address']['path'])
                                except KeyError:
                                    town = ""

            try:
                county = unicode(mapobj['address']['county'])
            except KeyError:
                county = ""

            try:
                state = unicode(mapobj['address']['state'])
            except KeyError:
                try:
                    state = unicode(mapobj['address']['state_district'])
                except KeyError:
                    state = ""

            try:
                country = unicode(mapobj['address']['country'])
            except KeyError:
                country = "No Data              Probably Ocean"

        oledExp.clear()

        oledExp.setCursor(0,0)
        oledExp.write(town)

        oledExp.setCursor(2,0)
        oledExp.write(county)

        oledExp.setCursor(4,0)
        oledExp.write(state)

        oledExp.setCursor(6,0)
        oledExp.write(country)

        time.sleep(5)
        oledExp.clear()
        count = 0
            
