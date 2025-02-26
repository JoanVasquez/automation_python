from bs4 import BeautifulSoup
import requests


def get_currency(in_currency, out_currency):
  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  currency_element = soup.find("span", class_="ccOutputRslt")

  if currency_element:
    currency = currency_element.get_text()
    currency = float(currency[:-4])
    return currency
  else:
    print("Currency conversion element not found.")


print(get_currency('EUR', 'AUD'))
