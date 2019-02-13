#https://kaijento.github.io/2017/05/06/web-scraping-nasa-image-of-the-day/

import json
import requests

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
r = requests.get(url)
print(r.json())

obj = r.json();

# use object['key'] to access the value in the data
print("\n")
print(obj['copyright'])


