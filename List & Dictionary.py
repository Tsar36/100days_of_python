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