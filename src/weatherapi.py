import requests
import sqlite3
from bs4 import BeautifulSoup

API_KEY = "51214d180a93bd48877c2342c3304098"

def get_cities():
    url = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the correct table on the Wikipedia page
    table = soup.find("table", {"class": "wikitable sortable"})

    if not table:
        print("❌ ERROR: Table not found on the Wikipedia page.")
        return []

    cities = []

    for row in table.find_all("tr")[1:11]:  # Top 10 cities
        cols = row.find_all("td")
        if len(cols) > 1:
            city = cols[1].text.strip()
            cities.append(city)

    return cities

def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(url)
    data = response.json()
    
    if "main" in data and "temp" in data["main"]:
        return data["main"]["temp"]
    else:
        print(f"⚠️ No temperature data for {city}")
        return None

def save_to_db(city, temperature):
    conn = sqlite3.connect("weather.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            city TEXT,
            temperature REAL
        )
    """)
    c.execute("INSERT INTO weather (city, temperature) VALUES (?, ?)", (city, temperature))
    conn.commit()
    conn.close()

