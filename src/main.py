from weatherapi import get_cities, get_weather, save_to_db

def main():
    cities = get_cities()
    for city in cities:
        temp = get_weather(city)
        if temp is not None:
            print(f"{city}: {temp}°C")
            save_to_db(city, temp)

if __name__ == "__main__":
    main()

