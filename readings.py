import time  
from w1thermsensor import W1ThermSensor
from array import *
import datetime
import json
import requests # importing the requests library
from json_tricks import dumps


sensor = W1ThermSensor()
API_ENDPOINT="http://geoffish.herokuapp.com/api/store_values/"

def get_temps():
    while True:
        data=[]
        now=datetime.datetime.now()
        temperature =(sensor.get_temperature())
        data.append({"temp":temperature,'date':now})
        js_data=dumps(data)
        print(dumps(data))
        time.sleep(10)
        #sending post request and saving response as response object
        r=requests.post(url=API_ENDPOINT, data={'data':js_data})
        print (r)


get_temps()

