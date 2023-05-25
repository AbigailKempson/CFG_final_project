#data from CSV file - CSV files on GIT - need to change the pathway.
all_launch_df = pd.read_excel("C:/Users/chhar/Documents/CFG Degree/DATA/Project/APIs/Rocket Atmospheric Impact/Launch and re-entry database.xlsx", sheet_name="2019 launches")
all_launch_df.head()

reentries_df = pd.read_excel("C:/Users/chhar/Documents/CFG Degree/DATA/Project/APIs/Rocket Atmospheric Impact/Launch and re-entry database.xlsx", sheet_name="2019 re-entries")
reentries_df.head()


#data from Space X API
#reading the data in a JSON format.
import requests
from pprint import pprint as pp

endpoint = 'https://api.spacexdata.com/v3/launches'

response = requests.get(endpoint)
data = response.json()
print(pp(data))

#creating a DF using the JSON file.
import pandas as pd
df = pd.read_json("https://api.spacexdata.com/v3/launches")
print(df)

#See Jupyter notebook to explain the code.
spacex_url="https://api.spacexdata.com/v4/launches/past"
response = requests.get(spacex_url)
json1 = response.json()
data = pd.json_normalize(json1)
data = data[['rocket', 'success', 'payloads', 'launchpad', 'cores', 'flight_number', 'date_utc']]
data['date'] = pd.to_datetime(data['date_utc']).dt.date

BoosterVersion = []
PayloadMass = []
Orbit = []
LaunchSite = []
Outcome = []
Flights = []
GridFins = []
Reused = []
Legs = []
LandingPad = []
Block = []
ReusedCount = []
Serial = []
Longitude = []
Latitude = []

def getBoosterVersion(data):
    for x in data['rocket']:
        response = requests.get("https://api.spacexdata.com/v4/rockets/"+str(x)).json()
        BoosterVersion.append(response['name'])

getBoosterVersion(data)

def getLaunchSite(data):
    for x in data['launchpad']:
        response = requests.get("https://api.spacexdata.com/v4/launchpads/"+str(x)).json()
        Longitude.append(response['longitude'])
        Latitude.append(response['latitude'])
        LaunchSite.append(response['name'])
getLaunchSite(data)

def getPayloadData(data):
    for loads in data['payloads']:
        for load in loads:
            response = requests.get("https://api.spacexdata.com/v4/payloads/"+load).json()
            PayloadMass.append(response['mass_kg'])
            Orbit.append(response['orbit'])

getPayloadData(data)

def getCoreData(data):
    for cores in data['cores']:
        for core in cores:
            if core['core'] != None:
                response = requests.get("https://api.spacexdata.com/v4/cores/"+core['core']).json()
                Block.append(response['block'])
                ReusedCount.append(response['reuse_count'])
                Serial.append(response['serial'])
            else:
                Block.append(None)
                ReusedCount.append(None)
                Serial.append(None)
            Outcome.append(str(core['landing_success'])+' '+str(core['landing_type']))
            Flights.append(core['flight'])
            GridFins.append(core['gridfins'])
            Reused.append(core['reused'])
            Legs.append(core['legs'])
            LandingPad.append(core['landpad'])
getCoreData(data)

launch_dict = {'FlightNumber': list(data['flight_number']),
'Date': list(data['date']),
'RocketName':BoosterVersion,
'PayloadMassKG':PayloadMass,
'Orbit':Orbit,
'LaunchSite':LaunchSite,
'Outcome':Outcome,
'Flights':Flights,
'GridFins':GridFins,
'Reused':Reused,
'Legs':Legs,
'LandingPad':LandingPad,
'Block':Block,
'ReusedCount':ReusedCount,
'Serial':Serial,
'Longitude': Longitude,
'Latitude': Latitude}

dflaunch = pd.DataFrame.from_dict(launch_dict, orient='index').transpose()

print(dflaunch.head(5))