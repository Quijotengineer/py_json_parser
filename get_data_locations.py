# https://realpython.com/beautiful-soup-web-scraper-python/

import requests
from bs4 import BeautifulSoup

URL = "https://github.expedia.biz/Brand-Expedia/lodging-pricing-ecap/blob/master/jobs-python/lodging_pricing_ecap/config/env/egdp-databricks.json"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

inputs = soup.find_all("span", class_="pl-pds")

# print(soup.prettify())

for input in inputs:
    print(input, end="\n"*2)