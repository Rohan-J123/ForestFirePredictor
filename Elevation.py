import requests
import json

def elevation(LATITUDE, LONGITUDE):
    url = "https://api.open-meteo.com/v1/elevation"

    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        if 'elevation' in data:
            print(f"Elevation: {data['elevation']} meters")
            return data['elevation']
        else:
            print("Elevation data not found in the response.")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

import time

file_path = "./Non_Fires_Datasets/Non_Fires_LAI_FPAR_2.geojson"
with open(file_path, 'r') as file:
    geo_data = json.load(file)
    output_data = []
    for feature in geo_data['features']:
        [LONGITUDE, LATITUDE] = feature['geometry']['coordinates']

        elevation_data = elevation(LATITUDE, LONGITUDE)

        feature["elevation_data"] = elevation_data
        output_data.append(feature)
        time.sleep(0.1)
    geo_data['features'] = output_data
with open("./Non_Fires_Elevation_2.geojson", 'w') as out_file:
      json.dump(geo_data, out_file, indent=4)