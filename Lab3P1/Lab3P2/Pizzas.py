class Pizza:
    def __init__(self, name,price, day = None, *args):
        if not isinstance(name, str):
            raise TypeError

        if not isinstance(price, int):
            raise TypeError
        self.name = name
        self.ingridients = args
        self.price = price
        self.day = day

    @staticmethod
    def __json__(item):
        return {'Name':item.name,'Ingridients':item.ingridients, 'Price': item.price, 'Day':item.day}


    def get_name(self):
        return self.name

    @staticmethod
    def get_pizza(name):
        return name.name

    def __str__(self):
        return f"{self.name} {self.day}"

class MondayPizza(Pizza):
    def __init__(self):
        self.name = "Margharitta"
        self.ingridients = "tomatoes", "tomato sause", "mozarella"
        self.price = 200
        self.day = "Monday"
        super().__init__(self.name, self.price, self.day, self.ingridients)

    def get_pizza(self):
        super().get_pizza(self.name)

    def __str__(self):
        return f"{self.name} {self.ingridients}"

class TuesdayPizza(Pizza):
    def __init__(self):
        self.name = "Pepperoni"
        self.ingridients = "olives", "bell pepper", "sausage"
        self.price = 210
        self.day = "Tuesday"
        super().__init__(self.name, self.price, self.day,self.ingridients)

    def __str__(self):
        return f"{self.name} {self.ingridients}"

class WednesdayPizza(Pizza):
    def __init__(self):
        self.name = "Chicago"
        self.ingridients = "italian sause", "pepperoni", "tomatoes"
        self.price = 400
        self.day = "Wednesday"
        super().__init__(self.name, self.price, self.day,self.ingridients)



    def __str__(self):
        return f"{self.name} {self.ingridients}"

class ThursdayPizza(Pizza):
    def __init__(self):
        self.name = "Cheese"
        self.ingridients = "mozzarella", "cheddar", "ricotta"
        self.price = 220
        self.day = "Thursday"
        super().__init__(self.name, self.price, self.day,self.ingridients)


    def __str__(self):
        return f"{self.name} {self.ingridients}"

class FridayPizza(Pizza):
    def __init__(self):
        self.name = "Hawaiian"
        self.ingridients = "pineapple", "cheese", "ham"
        self.price = 100
        self.day = "Friday"
        super().__init__(self.name, self.price, self.day,self.ingridients)


    def __str__(self):
        return f"{self.name} {self.ingridients}"

class SaturdayPizza(Pizza):
    def __init__(self):
        self.name = "Meat"
        self.ingridients = "bacon", "meatballs", "prosciutto"
        self.price = 120
        self.day = "Saturday"
        super().__init__(self.name, self.price, self.day,self.ingridients)


    def __str__(self):
        return f"{self.name} {self.ingridients}"

class SundayPizza(Pizza):
    def __init__(self):
        self.name = "Napoletana"
        self.ingridients = "tomatoes", "mozzarella", "olive"
        self.price = 320
        self.day = "Sunday"
        super().__init__(self.name, self.price, self.day,self.ingridients)


    def __str__(self):
        return f"{self.name} {self.ingridients}"