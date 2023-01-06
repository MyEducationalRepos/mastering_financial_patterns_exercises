from dotenv import load_dotenv
import pandas as pd
import os
import finnhub

load_dotenv()
token = os.getenv('API_KEY')


finnhub_client = finnhub.Client(api_key=token)

print(finnhub_client.stock_dividends('KO', _from='2019-01-01', to='2022-01-01'))
