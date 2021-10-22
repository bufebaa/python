import re

class Customer:
    def __init__(self, name, surname, patronymic, mobile_phone, *args):
        if not isinstance(name, str): raise TypeError
        self.__name = name
        if not isinstance(surname, str) : raise TypeError
        self.__surname = surname
        if not isinstance(patronymic, str) : raise TypeError
        self.__patronymic = patronymic
        pattern = re.compile("^\\+[0-9]{3}\\((\\d{2})\\)-\\d{3}-\\d{2}-\\d{2}")
        if not pattern.match(mobile_phone): raise TypeError
        self.__mobile_phone = mobile_phone


    @property
    def mobile_phone(self):
        return mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, name):
        pattern = re.compile("^\\+[0-9]{3}\\((\\d{2})\\)-\\d{3}-\\d{2}-\\d{2}")
        if not pattern.match(mobile_phone): raise TypeError
        self.mobile_phone = mobile_phone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        if not isinstance(name, str): raise TypeError
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str): raise TypeError
        self.__surname = surname

    @property
    def patronymic(self):
        return self.patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        if not isinstance(patronymic, str): raise TypeError
        self.__patronymic = patronymic

    def __str__(self):
        return f"{self.__name} {self.surname} {self.__patronymic}  Phone: {self.__mobile_phone}"

class Product:
    def __init__(self, id, name,price, dimension=0) :
        if not isinstance(id, int): raise TypeError
        self.Id = id
        if not isinstance(name, str): raise TypeError
        self.name = name
        if not isinstance(price, float): raise TypeError
        if not price >= 0 : raise TypeError
        self.price = price

    def get_name(self):
        return self.name
    @property
    def name(self):
         return self.__name
    @name.setter
    def name(self, name):
        if not isinstance(name, str): raise TypeError
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, float): raise TypeError
        if price < 0: raise ValueError
        self.__price = price

    def __str__(self):
        return f"Id: {self.Id} | Name: {self.name} | Price: {self.price}"

class Order:
    def __init__(self, customer, *products):
        if not isinstance(customer, Customer): raise TypeError
        for i in products:
            if not isinstance(i, Product): raise TypeError

        self.customer = customer
        self.products = products

    def add_product(self,*product):
        for i in product:
            if not isinstance(i, Product): raise TypeError
        temp = list(self.products)

        for i in range(len(product)):
            temp.append(product[i])
        self.products = tuple(temp)

    def del_product(self, *product):
        for i in product:
            if not isinstance(i, Product): raise TypeError
        temp = list(self.products)

        for i in range(len(product)):
            if product[i] in temp:
                temp.remove(product[i])
        self.products = tuple(temp)


    def total_value(self):
        total_cost = 0
        for i in self.products:
            total_cost += i.price

        return round(total_cost,4)

    def __str__(self):
        lst = []
        for i in self.products:
            lst.append(i.name)
        return f"{self.customer}\nProducts: {lst}\nTotal value = "+str(self.total_value())

product1 = Product(1, "Cardigan", 123.25, 300)
product2 = Product(2, "Hat", 456.35, 100)
product3 = Product(3, 'Socks', 45.6, 200)

Dasha = Customer("Dasha", "Kravchenko", "Alexandrovna", "+380(50)-180-34-34")

oder = Order(Dasha, product1,product2)
print(oder)
oder.del_product(product3)
print(oder)