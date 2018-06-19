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
                town = unicode(mapobj['address']['city'], "utf-8")
            except KeyError:
                try:
                    town = unicode(mapobj['address']['town'], "utf-8")
                except KeyError:
                    try:
                        town = unicode(mapobj['address']['village'], "utf-8")
                    except KeyError:
                        try:
                            town = unicode(mapobj['address']['hamlet'], "utf-8")
                        except KeyError:
                            try:
                                town = unicode(mapobj['address']['water'], "utf-8")
                            except KeyError:
                                try:
                                    town = unicode(mapobj['address']['path'], "utf-8")
                                except KeyError:
                                    town = unicode("", "utf-8")

            try:
                county = unicode(mapobj['address']['county'], "utf-8")
            except KeyError:
                county = unicode("", "utf-8")

            try:
                state = unicode(mapobj['address']['state'], "utf-8")
            except KeyError:
                try:
                    state = unicode(mapobj['address']['state_district']), "utf-8"
                except KeyError:
                    state = unicode("", "utf-8")

            try:
                country = unicode(mapobj['address']['country'], "utf-8")
            except KeyError:
                country = unicode("No Data              Probably Ocean", , "utf-8")

        oledExp.clear()

        oledExp.setCursor(0,0)
        oledExp.write(unicode(town), "utf-8")

        oledExp.setCursor(2,0)
        oledExp.write(unicode(county), "utf-8")

        oledExp.setCursor(4,0)
        oledExp.write(unicode(state), "utf-8")

        oledExp.setCursor(6,0)
        oledExp.write(unicode(country), "utf-8")

        time.sleep(5)
        oledExp.clear()
        count = 0
            
