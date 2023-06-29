#
travel_log = {
   "France" : {
       "total_visits" : 5,
       "cities_visited": ["Paris", "Lille", "Dijon"]},

   "Germany" : {
       "total_visits" : 3,
       "cities_visited" : ["Berlin", "Hamburg", "Stutgart"]},
}

country = input("\nCountry: ")
visits = int(input("Number of visits: "))
cities = input("Cities visited: ").split(', ')

travel_log[country] = {"total_visits" : visits,
"cities_visited" : cities} 

print(f"\n\n{'='*40}")

for i in travel_log:
    print(f"{i} {travel_log[i]}\n")

print(f"{'='*40}")


