from Pizzas import Pizza, MondayPizza, TuesdayPizza, WednesdayPizza, ThursdayPizza, SundayPizza, SaturdayPizza
from Menu import Menu
from File_creator import create_filesO, create_filesP
from Order import Order
import datetime
import json


create_filesP()
Liza = MondayPizza()
tuesday = TuesdayPizza()
menu = Menu(Liza, tuesday)
pizza = Pizza("Local", 232, "souse", "extra cheese", "tomatoes")
pizza2 = Pizza("NonStop", 232, "souse", "extra extra cheese", "double tomatoes")
menu.add_to_menu(pizza)
menu.add_to_menu(pizza2)
create_filesO()
Dasha = Order("Dasha")
print(Dasha)
Dasha.add_item()
print(Dasha)
Dasha.add_item(pizza)
print(Dasha)
Dasha.add_item()
Dasha.add_item(pizza2)