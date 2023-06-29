"""

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stutgart"],
}

"""


travel_log = {
   "France" : {
       "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits" : 5,
    },

   "Germany" : {
       "cities_visited" : ["Berlin", "Hamburg", "Stutgart"], "total_visits" : 3,
    },

}



#print("\n\n")
#print(travel_log)

#print(travel_log["Germany"])



for countries in travel_log:
    print("\n",countries, travel_log[countries])





