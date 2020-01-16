import requests
import json
import time

base_url = "https://www.wienerlinien.at/ogd_realtime"
monitor_url = "{}/monitor".format(base_url)

data_dir = "/home/pi/arduino/data"

def parse_status_code(code):
	if code == 200:
		return "OK"
	if code == 311:
		return "DB nicht verfuegbar"
	if code == 312:
		return "Haltepunkt existiert nicht"
	if code == 316:
		return "max. Anfragen ueberschritten"
	if code == 317:
		return "Sender existiert nicht"
	if code == 320:
		return "GET Anfrage Parameter invalid"
	
	return "Unknown status code {}".format(code)

def parse_departure(json_response):
	return json_response['data']['monitors'][0]['lines'][0]['departures']['departure']	

rbl_pha = 165 # richtung prater hauptallee
rbl_sfp = 172 # richtung stefan fadinger platz

rbl = [rbl_pha, rbl_sfp]

for direction in rbl:
	response = requests.get(monitor_url, params=[("rbl", direction)])

	print(parse_status_code(response.status_code))
	response_json = response.json()

	with open("{}/data_{}.json".format(data_dir, direction), 'w') as f:
		json.dump(response_json, f)
		f.close()

	time.sleep(5)




