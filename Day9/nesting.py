# NESTING

capitals = {
    'Kneya': 'Nairobi',
    'France': 'Paris'
}

# NESTING A LIST IN DICTIONARY

travels = {
    'Kenya': ['Nairobi', 'Nakuru', 'Narok', 'Nanyuki', 'Namanga']
}

# NESTING DICTIONARY INSIDE A DICTIONARY

travel = {
    'Kenya': {'places_visited': ['Nairobi', 'Nakuru', 'Narok', 'Nanyuki', 'Namanga'], 'total_visits': 12 }
}

# NESTING DICTIONARY IN A LIST

trv = [
    {'country': 'Kenya',
    'places_visited': ['Nairobi', 'Nakuru'],
    'total_visits': 12
    },
]

# qqqqqqqqqqqqqqqqqqqqqqqqqqqqqq

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

new_entry = {}
def add_new_country(name, num, city):
    new_entry = {
        'country': name,
        'visits': num,
        'cities': city
    }
    travel_log.append(new_entry)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)