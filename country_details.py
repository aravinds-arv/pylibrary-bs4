import requests
from bs4 import BeautifulSoup

URL = "https://www.scrapethissite.com/pages/simple"
r = requests.get(URL)

soup = BeautifulSoup(r.text, "lxml")
country_section = soup.find("section", id="countries")
div = country_section.find("div", class_="container")
rows = div.find_all("div", class_="row")[3:]
row = rows[0]

for row in rows:
    countries = row.find_all("div", class_="col-md-4 country")
    for country in countries:
        name = country.h3.text.strip()
        country_info = country.find("div", class_="country-info")
        country_spans = country.find_all("span")
        capital = country_spans[0].text
        population = country_spans[1].text
        area = country_spans[2].text
        print(f'''Country: {name}
Capital: {capital}
Populaton: {population}
Area(km^2): {area}
''')
    break