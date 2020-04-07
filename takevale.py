# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time
import csv
import statistics as st
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Software SPI configuration:
#CLK  = 18
#MISO = 23
#MOSI = 24
#CS   = 25
#mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('values')
ini=0
su=0
while ini<10:
	ini=ini+1
	value=mcp.read_adc(0)
	su=su+value
	time.sleep(0.5)

ref=su/10
k=[]	
g=0
pre=0
sref=ref
# Main program loop.
while True:
    value = mcp.read_adc(0)
    if value>=ref-20 or value<=10:
        print("not connected")
        con=0
    else:
        con=((1024+2*value)*10000)/(ref-value)
        #g=g+1
        with open('cad1.csv','a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([value])
	print(str(con)+" "+str(value))
	k.append(value)
	if len(k)>=30 and g ==0:
		sref=st.mode(k)
		g=1
		k=[]
	elif len(k)>=30:
		with open('ca.csv','a') as csvfile:
                	writer = csv.writer(csvfile)
                	writer.writerow([sref])
		if pre>0:
			sref=pre
		pre=st.mode(k)
		print("Present mode value is "+str(pre)+" Previous mode is "+str(sref))
		k=[]
		value= abs(sref-pre)
		if value>=100 and value<150:
			print("Getting disturbed?")
			print("Relax stay calm, deviate your thought")
        	elif value>=150 and value<200:
			print("Lost in thougts")
			print("Music lover?")
			print("Song specially for you")
			os.system('./music.sh')
        	elif value>=200:
			print("why so sad")
			print("share your pain")
			mes="John is not feeling well, his sensor reads "+str(value)
			emergency.group(["doctor@gmail.com"],mes,"Patient alert")	
    time.sleep(0.5)

