# Author: zem_232 for PUI 2018 at CUSP, NYU, NYC
##############################
# Part 4 of HW3 
# MTA Bus Tracking with SIRI API
# Writing next stop info to .csv
##############################
# put your name as input argument:
# i.e. run the code as
#      python show_bus_locations_zem_232.py <API_key> <Bus_line> <Bus_line>.csv

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
if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python show_bus_locations_zem_232.py <API_key> <Bus_line> <Bus_line>.csv")
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

fout=open(sys.argv[3],"w")
fout.write("latitude,longitude,Stop Name,Stop Status\n")

for k in np.arange(n):
    lat=dataDict_meat[k]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    long=dataDict_meat[k]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    if dataDict_meat[k]['MonitoredVehicleJourney']['OnwardCalls']==0:
        stop="N/A"
        status="N/A"
    else:
        stop=dataDict_meat[k]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        status=dataDict_meat[k]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    fout.write('{lat},{long},{stop},{status}\n'.format(n=k,lat=lat,long=long,stop=stop,status=status))
