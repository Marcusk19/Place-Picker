import random
# import pandas as pd, numpy as np
import requests
import json
import time
from picker import ipHandler
from picker import config

ip_info_token = "09adbd3b4440a4"

def pickPlace():
    # declare an array of places to choose from
    all_places = []
    keywords = ['restaurant']
    api_key = config.api_key
    radius = '1000'
    coordinates = ipHandler.get_location() # obtain coords from ip addr
    city = ipHandler.get_city()
    print('Searching {0} within radius {1}...'.format(city, radius))
    # print(coordinates)

    for keyword in keywords:
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+coordinates+'&radius='+str(radius)+'&keyword='+str(keyword)+'&key='+str(api_key)
        while(True):
        # print(url)
            respon = requests.get(url)
            jj = json.loads(respon.text)
            results = jj['results']
            for result in results:
                name = result['name']
                place_id = result['place_id']
                lat = result['geometry']['location']['lat']
                lng = result['geometry']['location']['lng']
                rating = result['rating']
                types = result['types']
                vicinity = result['vicinity']
                place = [name, place_id, lat, lng, rating, types, vicinity]
                all_places.append(place)

            if 'next_page_token' not in jj:
                break
            else:
                next_page_token = jj['next_page_token']
                url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key='+str(api_key)+'&pagetoken='+str(next_page_token)
                continue
        labels = ['Place Name', 'Place ID', 'Latitude', 'Longitude', 'Rating', 'Types', 'Vicinity']
            #    [    0            1            2           3           4          5         6    ]
        
        # code that exports data to csv file if needed
        # export_dataframe_1_medium = pd.DataFrame.from_records(all_places, columns=labels)
        # export_dataframe_1_medium.to_csv('export_dataframe_1_medium.csv')
        
    x = 0
    y = len(all_places) - 1
    random_index = random.randint(x,y)

    name = all_places[random_index][0]
    rating = all_places[random_index][4]
    address = all_places[random_index][6]
    time.sleep(3)
    # print('I suggest "{0}" with a rating of {1} at "{2}"'.format(name, rating, address))
    return "I suggest " + str(name) + " with a rating of " + str(rating) + " at " + str(address)


def hello():
    print('Hello from place picker!')