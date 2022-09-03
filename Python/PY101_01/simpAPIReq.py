from sqlite3 import Date
import requests
import time
import json


# while True:
req = requests.get("https://swapi.dev/api/people/2/")
# print(req.status_code)

# if req.status_code != 200:
#     pass

person = req.json()
name = person["name"]
birthyear = person["birth_year"]

# print(person)



print(f"Name is\t\t\t{name}")
print(f"Birth year is\t\t{birthyear}")

# print(person["name"])# print(Date.day)
# time.sleep(5)

for film in person["films"]:
    req = requests.get(film)
    film = req.json()
    print("Film is : ", film["title"])




