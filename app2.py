from dotenv import load_dotenv
import pandas as pd
import os
import requests
from requests.auth import HTTPBasicAuth







load_dotenv()
token = os.getenv('POLIGON_KEY')
auth = HTTPBasicAuth(api_user, api_token)

headers = {
  "Accept": "application/json"
}





url = 'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2020-06-01/2020-06-17?apiKey='+token

projects_response = requests.request(
   "GET",
   url)

print(projects_response.text)