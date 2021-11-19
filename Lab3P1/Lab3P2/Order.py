import json
import datetime
from Pizzas import Pizza, MondayPizza, TuesdayPizza, WednesdayPizza, ThursdayPizza, SundayPizza, SaturdayPizza, FridayPizza
from File_creator import create_filesO

class Order:

    def __init__(self, name, pizzas_name=None):
        self.__name = name
        self.cart = []
        if pizzas_name is not None:
            if not isinstance(pizzas_name, Pizza):
                raise TypeError
            self.cart.append(pizzas_name)
        else:
            self.cart.append(self.check_the_date(datetime.datetime.today().weekday()))

        self.__json__()

    def total_sum(self):
        sum = 0
        for i in self.cart:
            sum += i.price
        return sum

    @staticmethod
    def check_the_date(date):
        if date == 0:
            return Pizza.get_pizza(MondayPizza())
        elif date == 1:
            return Pizza.get_pizza(TuesdayPizza())
        elif date == 2:
            return Pizza.get_pizza(WednesdayPizza())
        elif date == 3:
            return ThursdayPizza()
        elif date == 4:
            return FridayPizza()
            # return Pizza.get_pizza(FridayPizza())
        elif date == 5:
            return Pizza.get_pizza(SaturdayPizza())
        elif date == 6:
            return Pizza.get_pizza(SundayPizza())


    def __str__(self):
        temp = ''
        for i in self.cart:
            temp += f"{i.name}/"
        return f'Name: {self.__name} \nOrder: {temp} pizza/s\nSum: {self.total_sum()}'

    def add_item(self, pizzas_name = None):
        if pizzas_name is not None :
            if not isinstance(pizzas_name, Pizza):
                raise TypeError
            self.cart.append(pizzas_name)
            self.__json__(pizzas_name)
        else:
            self.cart.append(self.check_the_date(datetime.datetime.today().weekday()))
            self.__json__(self.check_the_date(datetime.datetime.today().weekday()))

    def __json__(self, args = None):
        if args == None:
            json_data = json.load(open('order.json', encoding='utf-8'))
            json_data['Clients'].append(self.json_add())
            json.dump(json_data, open('order.json', mode='w', encoding='utf-8'), indent=4)
        else:
            create_filesO()
            json_data = json.load(open('order.json', encoding='utf-8'))
            json_data['Clients'].append(self.json_add())
            json.dump(json_data, open('order.json', mode='w', encoding='utf-8'), indent=4)


    def json_add(self):
        temp = []
        sum = 0
        for i in self.cart:
            temp.append(i.name)
        return {'Name':self.__name, 'Order':temp, 'Total sum is':self.total_sum()}





