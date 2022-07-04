# List and Dictionary

# {
#   "Key": [List],
#   "Key2": {Dictionary},
# }

# Nesting:

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visited": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgard"], "total_visited": 10},
}
print(travel_log["France"])

travel_log2 = [
  {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visited": 12
  },
  {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgard"],
    "total_visited": 10
  },
]
print(travel_log2[0])

# ------------------------------ Exercise:

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
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_visited, times_visited, cities_visited):
    new_country ={}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
