import requests
import json

base_url = "https://www.wienerlinien.at/ogd_realtime"
monitor_url = "{}/monitor".format(base_url)


rbl_pha = 165 # richtung prater hauptallee
rbl_sfp = 172 # richtung stefan fadinger platz

response = requests.get(monitor_url, params=[("rbl", 165), ("sender", "")])

departures = response.json()['data']['monitors'][0]['lines'][0]['departures']['departure']

for departure in departures:
	print(departure["departureTime"])





