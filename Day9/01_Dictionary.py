programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again.", 
                          }

#Retrieving items from dictionary.
# print(programming_dictionary["Function"])

#Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# print(programming_dictionary)

#Create empty dictionary
create_empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in computer system"
# print(programming_dictionary)

#Loop though dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


#Nesting
capitals = {"Fance" : "Paris",
            "German" : "Berlin",
}

#Nesting a List in a Dictionary

travel_log  = {
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Berlin","Hamburg","Stuttgart"],
    }

#Nesting Dictionary in a Dictionary

travel_log  = {
    "France": {"Cities_visited":["Paris","Lille","Dijon"],"total_visits":12},
    "Germany":{"Cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visits":8},
    }
print(travel_log)

#Nesting Dictionary in a List

travel_log  = [
    {
        "Country": "France", 
        "Cities_visited":["Paris","Lille","Dijon"],
        "total_visits":12
    },
    {
        "Country": "Germany",
        "Cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits":8
    },
    ]
print(travel_log)