import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

st.header('Indian Stock Dashboard')

ticker = st.sidebar.text_input('Symbol Code', 'INFY')
exchange = st.sidebar.text_input('Exchange', 'NSE')

url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Safely extracting price and handling NoneType issues
price_tag = soup.find(class_="YMlKec fxKbKc")
previous_close_tag = soup.find(class_="P6K39c")
revenue_tag = soup.find(class_="QXDnM")
news_tag = soup.find(class_="YFvfS")
about_tag = soup.find(class_="bllb2d")

# Default values if any tag is None
price = float(price_tag.text.strip()[1:].replace(",", "")) if price_tag else 'N/A'
previous_close = float(previous_close_tag.text.strip()[1:].replace(",", "")) if previous_close_tag else 'N/A'
revenue = revenue_tag.text if revenue_tag else 'N/A'
news = news_tag.text if news_tag else 'N/A'
about = about_tag.text if about_tag else 'N/A'

dict1 = {
    'Price': price,
    'Previous Price': previous_close,
    'Revenue': revenue,
    'News': news,
    'About': about
}

df = pd.DataFrame(dict1, index=['Extracted Data']).T

st.write(df)
