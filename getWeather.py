# Get weather data from Ilmatieteenlaitos for Tampere
# temperature, rain, wind, wind_direction

import requests
import xml.etree.ElementTree as ET
from datetime import datetime

"""

      Example formation for location and time 
       String place = "Tampere";
        String startTime = "2023-10-24T00:00:00Z";
        String endTime = "2023-10-24T23:59:59Z";
        Returns data in format hours:temperature:rain (mm)
        
    
"""

def getWeather():
    """
    fetch weather data for Tampere from url and return it as a list of strings
    return data format: hours:temperature:rain:windspeed:wind_direction

    """
    place = "Tampere"

    baseUrl = "http://opendata.fmi.fi/wfs"
    query = "fmi::forecast::harmonie::surface::point::multipointcoverage"

    parameters = "temperature,precipitation1h,winddirection,windspeedms"

    url = baseUrl + "?service=WFS&AcceptFormats=application/json&version=2.0.0&request=getFeature&storedquery_id=" + query+ "&place=" + place + "&parameters=" + parameters
    
    #print(url)
    
    try:
        
        # get data from url, it is in wfs format
        response = requests.get(url)
        #print("response code (getWeather): " + str(response.status_code))

        # convert wfs to xml and find doubleOrNilReasonTupleList where wanted data is
        xml_content = response.content
        
        root = ET.fromstring(xml_content)
        
        element = root.find(".//{http://www.opengis.net/gml/3.2}doubleOrNilReasonTupleList")
        data = element.text.strip().split()
        
        # parse data and add hour to it
        # hours starts from current hour
        
        data = [data[i:i+4] for i in range(0, len(data), 4)]
        hours = [str(i)  for i in range(datetime.now().hour,datetime.now().hour + len(data))]
        
        data = [str(j + ":" + ":".join(i)) for i, j in zip(data, hours)]

        return data
         
    except:
        print("error")
        return "error"
            
    

    