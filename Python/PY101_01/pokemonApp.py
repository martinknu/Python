# Ask for user input
# Create a dynamic url based on prev. step
# Fetch data from URL
# Convert JSON to Dict
# Print pokemon data

import requests

while True:

    inpString = input("Which pokemon do you want to search for?")
    searchP1 =  "https://pokeapi.co/api/v2/pokemon/"
    # searchP2 =  
    searchString =  searchP1 + inpString 
    searchString = searchString.lower()
    
    print(searchString)


    req = requests.get(searchString)

    if req.status_code == 200:
        pokemon = req.json()
        # print(pokemon)
        print(f"Name is \t\t", pokemon["name"])

        for ability in pokemon["abilities"]:
            print(ability)
    else:
        print("Pokemon not found")