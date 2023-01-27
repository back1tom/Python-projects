#Nesting Dictionary in a Dictionary

travel_log = {
    "Poland": {"cities_visited": ["Warszawa", "Wrocław", "Gdańsk", "Świdnica"], "total_visits": 10},
    "Germany": {"cities_visited": ["Berlin", "Frankfurt", "Munich", "Hamburg"], "total_visits": 8},
}

#Nesting Dictionary in a List

travel_log = [
    {
        "country": "Poland",
        "cities_visited": ["Warszawa", "Wrocław", "Gdańsk", "Świdnica"],
        "total_visits": 10
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Frankfurt", "Munich", "Hamburg"],
        "total_visits": 8
    },
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)