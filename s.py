import requests, json

def json_print(obj):
    t = json.dumps(obj, sort_keys=True, indent=4)
    return t

def print_header():
    print('*' * 50)
    print('Developer: Kyle McCarthy')
    print('Description: This program will use the Open Notify API to display information from NASA regarding astronauts currently in space.')
    print('*' * 50)


response = requests.get("http://api.open-notify.org/astros.json")

obj = json_print(response.json())

x = json.loads(obj)

msg = x["message"]
people = x["people"]
number_in_space = x["number"]


print_header()
print(f"API return: {msg}")
print(f'\nNumber of people in space: {number_in_space}')
print('\nCraft and astronaut information:')

for person in people:
    for k,v in person.items():
        print(f'{k.title()}: {v}')