import time
import csv
import emergency
import statistics as st
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import os

SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


print('Reading MCP3008 values...')
print('values')
ref=512
ctr=0
g=0
# Main program loop.
while True:
    value = mcp.read_adc(0)
    if value>=ref or value<=10:
        print("Not human")
    else:
        with open('values.csv','a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([value])
        print(str(value))
        if g==1 and ctr==60:
                g=0
                ctr=0
        elif g==2 and ctr==10:
                g=0
                ctr=0
        elif g!=0:
                ctr=ctr+1
        elif value<400 and value>=350:
                print("Getting disturbed?")
                print("Relax stay calm, deviate your thought")
                g=1
        elif value<350 and value>=200:
                print("Lost in thougts")
                g=2
                print("Music lover?")
                print("Song specially for you")
                os.system('./music.sh')
        elif value<200:
                print("why so sad")
                print("share your pain")
                mes="John is not feeling well, his sensor reads "+str(value)
                emergency.group(["patchavageethika@gmail.com"],mes,"Patient alert")
                g=3
        else:
                print("normal")

    time.sleep(1)

