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
        oledExp.setCursor(0,0)
        oledExp.write(currenttime)

    if currentdate != prevdate:
        oledExp.setCursor(2,0)
        oledExp.write(currentdate)

    currentlat = obj['iss_position']['latitude']
    if currentlat != prevlat:
        oledExp.setCursor(4,0)
        if float(currentlat) < 0:
            oledExp.write(str(currentlat)[1:] + ' S')
        else:
            oledExp.write(str(currentlat) + ' N')

    currentlon = obj['iss_position']['longitude']
    if currentlon != prevlon:
        oledExp.setCursor(6,0)
        if float(currentlon) < 0:
            oledExp.write(str(currentlon)[1:] + ' S')
        else:
            oledExp.write(str(currentlon) + ' N')
