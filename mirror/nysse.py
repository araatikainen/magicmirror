import json
import requests

"""
Tässä on asiakassovelluksen salaisuus, jota tarvitset autentikoitumiseen.
Asiakas-ID
9765096899212087
Asiakassovelluksen salaisuus
zint5yTdlHX1jAG3MKuZZ2SjcVyo6DlS
Tallenna salaisuus turvalliseen paikkaan. Salaisuus ei ole näkyvillä täällä tämän jälkeen. Jos hävität salaisuuden, se pitää luoda uudelleen.

id = "9765096899212087"
apiKey = "zint5yTdlHX1jAG3MKuZZ2SjcVyo6DlS"
url = "https://data.waltti.fi"
"""


url = 'https://api.digitransit.fi/routing/v1/routers/waltti/index/graphql'
name = 'digitransit-developer-api'
key = '774fe955df6d4cfc8411cdb67fc6969d'

headers = {
    "digitransit-subscription-key" : "774fe955df6d4cfc8411cdb67fc6969d"
}

# graphql for getting stop 0831 Opiskelija A and five next departures
body = """
    {
        stop(id: "tampere:0831" ) {
          name
          code
          routes {
            shortName
            longName
          }
          stoptimesWithoutPatterns(numberOfDepartures: 5) {
          scheduledArrival
          }
        }
    }
    """

# get data from url using graphlq body and headers 
# return json object
def getData():
    url = 'https://api.digitransit.fi/routing/v1/routers/waltti/index/graphql'
    body = """
        {
            stop(id: "tampere:0831" ) {
            name
            code
            routes {
                shortName
                longName
            }
            stoptimesWithoutPatterns(numberOfDepartures: 5) {
            scheduledArrival
            }
            }
        }
        """
    response = requests.post(url=url, json={"query": body}, headers=headers)
    #print("responsecode: ", response.status_code)
    if response.status_code == 200:
        return json.loads(response.text).get('data').get('stop')
    else:
        return "Error"

"""
data = getData(url, body)
print(data)

print(data.get('stoptimesWithoutPatterns'))

print(data.get('name'))
print(data.get('routes')[0].get('longName'))
for i in data.get('stoptimesWithoutPatterns'):
    hours = int(i.get('scheduledArrival'))//(60*60)
    minutes = int(i.get('scheduledArrival'))//60 - hours*60
    print(hours, ":", minutes)
"""