import json
def create_filesP():
    to_json = {'Pizzas': []}
    with open('menu.json', 'w') as file:
        json.dump(to_json, file, indent=3)

def create_filesO():
    to_json = {'Clients': []}
    with open('order.json', 'w') as file:
        json.dump(to_json, file, indent=3)