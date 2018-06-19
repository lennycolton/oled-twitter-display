import urllib2
import json

req = urllib2.Request("http://api.open-notify.org/iss-now.json")
response = urllib2.urlopen(req)
obj = json.loads(response.read())

mapreq = urllib2.Request("http://nominatim.openstreetmap.org/reverse?format=json&lat=" + obj['iss_position']['latitude'] + "&lon=" + obj['iss_position']['longitude'] + "&zoom=18&addressdetails=1")
mapresponse = urllib2.urlopen(req)
mapobj = json.loads(response.read())
print(mapobj) 
