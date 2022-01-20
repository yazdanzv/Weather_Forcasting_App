from tkinter import *
import requests


ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
KEY = "58cd189feef4d9f808fc5630caf130a1"

class Weather:
    def __init__(self):
        self.city = "Karaj"
        self.weather = {
            "lat": 35.807580,
            "lon": 50.987420,
            "appid": KEY,
            "units": "imperial"
        }
        self.response = requests.get(ENDPOINT, params=self.weather)
        self.response.raise_for_status()
        print(self.response.json())


Weather()