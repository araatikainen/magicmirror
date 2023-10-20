import json
import requests

"""
Tässä on asiakassovelluksen salaisuus, jota tarvitset autentikoitumiseen.
Asiakas-ID
9765096899212087
Asiakassovelluksen salaisuus
zint5yTdlHX1jAG3MKuZZ2SjcVyo6DlS
Tallenna salaisuus turvalliseen paikkaan. Salaisuus ei ole näkyvillä täällä tämän jälkeen. Jos hävität salaisuuden, se pitää luoda uudelleen.
"""
id = "9765096899212087"
apiKey = "zint5yTdlHX1jAG3MKuZZ2SjcVyo6DlS"

url = "https://data.waltti.fi"

tripUrl = url + "/tampere/api/gtfsrealtime/v1.0/feed/tripupdate"
posUrl = url + "/tampere/api/gtfsrealtime/v1.0/feed/vehicleposition"
alertUrl = url + "/tampere/api/gtfsrealtime/v1.0/feed/servicealert"


def getTripData():
    response = requests.get(tripUrl, auth=(id, apiKey))
    print("response code (getTripData): " + str(response.status_code))
    return response.text

def getPosData():
    response = requests.get(posUrl, auth=(id, apiKey))
    print("response code (getPosData): " + str(response.status_code))
    return response.text

def getAlertData():
    response = requests.get(alertUrl, auth=(id, apiKey))
    print("response code (getAlertData): " + str(response.status_code))
    return response.text

# change string to json

#tripData = json.loads(getTripData())
#posData = json.loads(getPosData())
#alertData = json.loads(getAlertData())

tripData = getTripData()
print(tripData)
print(isinstance(tripData, dict))
#print(tripData)
#print(posData)
#print(alertData)
