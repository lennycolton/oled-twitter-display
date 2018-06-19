import time
from OmegaExpansion import oledExp

oledExp.driverInit()
oledExp.clear()

currenttime = ""
currentdate = ""

while True:
        prevtime = currenttime
        prevdate = currentdate
        currenttime = time.strftime("%H:%M:%S")
        currentdate = time.strftime("%a, %d/%m/%Y")

        if currenttime != prevtime:
                oledExp.setCursor(2,0)
                oledExp.write(currenttime)

        if currentdate != prevdate:
                oledExp.setCursor(5,0)
                oledExp.write(currentdate)
