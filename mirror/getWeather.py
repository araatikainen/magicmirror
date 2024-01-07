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
    return data format: hours:temperature:rain:wind_direction:windspeed

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
        
        # parse data and calculate averages in three hour intervals for the next 12 hours
        
        data = [data[i:i+4] for i in range(0, len(data), 4)]

        interval = 3
        hours = 12
        parsedData = [{"time" : datetime.now().hour,"temperature" : round(float(data[0][0])), "rain" : round(float(data[0][1])), "wind_direction" : data[0][2], "wind_speed" : round(float(data[0][3]))}]

        for i in range(0, hours, interval):
            
            time = datetime.now().hour + i + interval
            if time > 23:
                time = time - 24

            avgTmp = round((float(data[i][0]) + float(data[i+1][0]) + float(data[i+2][0]))/3, 1)
            avgRain = round((float(data[i][1]) + float(data[i+1][1]) + float(data[i+2][1]))/3, 1)
            avgWindDir = round((float(data[i][2]) + float(data[i+1][2]) + float(data[i+2][2]))/3, 1)
            avgWindSpeed = round((float(data[i][3]) + float(data[i+1][3]) + float(data[i+2][3]))/3, 1)

            parsedData.append({"time" : time,"temperature" : avgTmp, "rain" : avgRain, "wind_direction" : avgWindDir, "wind_speed" : avgWindSpeed})

        return parsedData
         
    except:
        print("error")
        return "Error"
            
  

#data = getWeather()
#print(data)