# Author: zem_232 for PUI 2018 at CUSP, NYU, NYC
##############################
# Part 3 of HW3 
# MTA Bus Tracking with SIRI API
##############################
# put your name as input argument:
# i.e. run the code as
#      python show_bus_locations_zem_232.py <API_key> <Bus_line>

# import python 2 print function package
from __future__ import print_function

import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys
import numpy as np

# make sure input arguments are correct
if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python show_bus_locations_zem_232.py <API_key> <Bus_line>")
    sys.exit()
    
if not len(sys.argv[2]) == 3:
    print ("Invalid MTA bus line.")
    sys.exit()
    
apikey = sys.argv[1]
bus = sys.argv[2]

url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey,bus)

print(url)
response=urllib.urlopen(url)
data=response.read().decode("utf-8")
dataDict=json.loads(data)

dataDict_meat=dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
# dataDict=dataDict['ServiceDelivery']
# dataDict=dataDict['VehicleMonitoringDelivery']
# dataDict=dataDict[0]
# dataDict=dataDict['VehicleActivity']
n=len(dataDict_meat)

print ("Bus line : %s"%(bus))
print ("Number of buses : %s"%(n))
for k in np.arange(n):
    lat=dataDict_meat[k]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    long=dataDict_meat[k]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print ('Bus {n} is at latitude {lat} and longitude {long}'.format(n=k,lat=lat,long=long))