import json
from Pizzas import MondayPizza, Pizza
class Menu:
    def __init__(self, *args):
        self.menu = args
        self.__json__()

    def add_to_menu(self, args):
        if not isinstance(args, Pizza):
            raise TypeError
        if self.is_unic(args):
            l = list(self.menu)
            l.append(args)
            self.menu = tuple(l)
            self.__json__(args)
        else:
            print("Sorry the name is being used")

    @staticmethod
    def is_unic(args):
        json_data = json.load(open('menu.json', encoding='utf-8'))
        for item in json_data['Pizzas']:
            if item["Name"] == args.get_name():
                return False
        return True

    @staticmethod
    def see_the_menu():
        with open('menu.json', 'r') as f:
            json_data = json.load(f)
        print(json.dumps(json_data, indent=2))

    def __json__(self, args=None):
        if args == None:
            json_data = json.load(open('menu.json', encoding='utf-8'))
            for i in self.menu:
                json_data['Pizzas'].append(i.__json__(i))
            json.dump(json_data, open('menu.json', mode='w', encoding='utf-8'), indent=4)
        else:
            json_data = json.load(open('menu.json', encoding='utf-8'))
            json_data['Pizzas'].append(args.__json__(args))
            json.dump(json_data, open('menu.json', mode='w', encoding='utf-8'), indent=4)





