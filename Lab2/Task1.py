class Customer:
    def __init__(self, name, surname, patronymic, mobile_phone):
        if not isinstance(name, str): raise TypeError
        self.name = name
        if not isinstance(surname, str) : raise TypeError
        self.surname = surname
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone

class Product:
    def __init__(self, product, price, weight) -> None:
        if not isinstance(product, str): raise TypeError
        self.name = product
        self.price = price
        self.weight = weight

class Order:
    def __init__(self, customer, *products):
        if not isinstance(customer, Customer): raise TypeError
        for i in products:
            if not isinstance(i, Product): raise TypeError

        self.customer = customer
        self.products = products

    def total_value(self):
        total_cost = 0
        for i in self.products:
            total_cost += i.price
        return total_cost

    def __str__(self):
        return self.customer.name+' '+self.customer.surname+'\nTotal value = '+str(self.total_value())

product1 = Product('Cardigan', 12334, 300)
product2 = Product('Hat', 456, 100)
Dasha = Customer("Dasha", "Kravchenko", "Alexandrovna", "+32423523425")

oder = Order(Dasha, product1,product2)
print(oder)
