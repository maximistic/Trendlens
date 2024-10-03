import requests
from bs4 import BeautifulSoup
import time 


url1 = 'https://www.google.com/finance/quote/INFY:NSE'
url2 = 'https://www.google.com/finance/quote/RELIANCE:NSE'
url3 = 'https://www.google.com/finance/quote/500209:BOM'

ticker = 'RELIANCE'
url = f'https://www.google.com/finance/quote/{ticker}:NSE'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find('div', {'class': 'YMlKec fxKbKc'}).text

print(price)