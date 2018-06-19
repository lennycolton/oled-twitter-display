import urllib2
import json
from OmegaExpansion import oledExp

req = urllib2.Request("http://api.open-notify.org/iss-now.json")
response = urllib2.urlopen(req)

obj = json.loads(response.read())

if oledExp.driverInit() != 0:
    print('ERROR: Could not initialise the OLED Expansion')
    exit()

oledExp.clear()

oledExp.setCursor(1,0)
oledExp.write('Timestamp:')

oledExp.setCursor(2,0)
oledExp.write(str(obj['timestamp']))

oledExp.setCursor(4,0)
lat = obj['iss_position']['latitude']
if float(lat) < 0:
    oledExp.write(str(lat)[1:] + ' S')
else:
    oledExp.write(str(lat) + ' N')

oledExp.setCursor(6,0)
lon = obj['iss_position']['longitude']
if float(lon) < 0:
    oledExp.write(str(lon)[1:] + ' W')
else:
    oledExp.write(str(lon) + ' E')
