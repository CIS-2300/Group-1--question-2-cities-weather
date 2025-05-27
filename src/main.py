from weatherapi import get_weather
import requests
from bs4 import BeautifulSoup

def get_cities():
    url = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"class": "wikitable sortable"})
    
    cities = []
    for row in table.find_all("tr")[1:11]:  # Get top 10 cities
        city_cell = row.find_all("td")[1]
        city = city_cell.text.strip()
        cities.append(city)
    
    return cities

def main():
    cities = get_cities()
    print("Fetching weather for top 10 U.S. cities...\n")

    for city in cities:
        weather = get_weather(city)
        print(weather)

if __name__ == "__main__":
    main()

