import pyshark
from datetime import datetime

#cap = pyshark.LiveCapture(interface='en0') #wlan0

# simple webproxy idea
# capture packets  continuously and saved them to pcap file
# read from file and add new capture data to web page, must have stop capture and new capture options
# and then expand simple description to full description
# build an api with this and make it work with this web app

now = datetime.now()
current_time = now.strftime("%d/%m/%Y %H:%M:%S")
cap = pyshark.FileCapture("logs/%s".format(current_time))