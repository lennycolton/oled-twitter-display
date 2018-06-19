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

while True:
    count = 0
    prevlat = currentlat
    prevlon = currentlon
    prevtime = currenttime
    prevdate = currentdate
    currenttime = time.strftime("%H:%M:%S")
    currentdate = time.strftime("%a, %d/%m/%Y")

    req = urllib2.Request("http://api.open-notify.org/iss-now.json")
    response = urllib2.urlopen(req)

    obj = json.loads(response.read())

    if not place:
        oledExp.setCursor(0,0)
        oledExp.write(currenttime)
        count = count + 1

    if not place:
        oledExp.setCursor(2,0)
        oledExp.write(currentdate)

    currentlat = obj['iss_position']['latitude']
    if currentlat != prevlat:
        if not place:
            oledExp.setCursor(4,0)
            if float(currentlat) < 0:
                oledExp.write(str(currentlat)[1:] + ' S            ')
            else:
                oledExp.write(str(currentlat) + ' N            ')

    currentlon = obj['iss_position']['longitude']
    if currentlon != prevlon:
        if not place:
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
                town = mapobj['city']
            except KeyError:
                try:
                    town = mapobj['town']
                except KeyError:
                    try:
                        town = mapobj['village']
                    except KeyError:
                        try:
                            town = mapobj['hamlet']
                        except KeyError:
                            town = ""

            try:
                county = mapobj['county']
            except KeyError:
                county = ""

            try:
                state = mapobj['state']
            except KeyError:
                state = ""

            try:
                country = mapobj['country']
            except KeyError:
                country = "No Data Probably Ocean"

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
            
