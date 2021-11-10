import json
import datetime
import time


class RagularTicket:
    price = 300
    def __init__(self, id):
        self.id = id
        json_data = json.load(open('my.json', encoding='utf-8'))
        if json_data['total_count']==0:raise ValueError("No left tickets")
        json_data['total_count']-=1
        json_data['Number of ragular'] += 1
        json_data['tickets'].append(self.__json__(self))
        json.dump(json_data, open('my.json', mode='w', encoding='utf-8'), indent=4)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    def __json__(self, item):
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        return {'Name of Ticket': item.__class__.__name__, 'Id': item.id, 'Price': item.price,
                'Date of purchase': str(datetime.date.today())+' '+current_time}

    def find_the_ticket(self, id):
        json_data = json.load(open('my.json', encoding='utf-8'))
        try:
            return next(item for item in json_data['tickets'] if item["Id"] == id)
        except (StopIteration):
            print("There is no such ticket:((((")

    def __str__(self):
        return f"Type of ticket:  {self.__class__.__name__}\nTicket id: {self.__id}\nPrice: {self.price}"



class AdvanceTicket(RagularTicket):
    def __init__(self, id):
        self.id = id
        self.price = RagularTicket.price*60/100
        json_data = json.load(open('my.json', encoding='utf-8'))
        if json_data['total_count'] == 0: raise ValueError("No left tickets")
        json_data['total_count'] -= 1
        json_data['Number of advance'] += 1
        json_data['tickets'].append(super().__json__(self))
        json.dump(json_data, open('my.json', mode='w', encoding='utf-8'), indent=4)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id



    def __str__(self):
        return f"Type of ticket:  {self.__class__.__name__}\nTicket id: {self.__id}\nPrice: {self.price}"

class StudentTicket(RagularTicket):
    def __init__(self, id):
        self.id = id
        self.price = RagularTicket.price/2
        json_data = json.load(open('my.json', encoding='utf-8'))
        if json_data['total_count'] == 0: raise ValueError("No left tickets")
        json_data['total_count'] -= 1
        json_data['Number of student'] += 1
        json_data['tickets'].append(super().__json__(self))
        json.dump(json_data, open('my.json', mode='w', encoding='utf-8'), indent=4)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    def __str__(self):
        return f"Type of ticket:  {self.__class__.__name__}\nTicket id: {self.__id}\nPrice: {self.price}"

class LateTickets(RagularTicket):
    def __init__(self, id):
        self.id = id
        self.price = RagularTicket.price+RagularTicket.price*10/100
        json_data = json.load(open('my.json', encoding='utf-8'))
        if json_data['total_count'] == 0: raise ValueError("No left tickets")
        json_data['total_count'] -= 1
        json_data['Number of late'] += 1
        json_data['tickets'].append(super().__json__(self))
        json.dump(json_data, open('my.json', mode='w', encoding='utf-8'), indent=4)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    def __str__(self):
        return f"Type of ticket:  {self.__class__.__name__}\nTicket id: {self.__id}\nPrice: {__price}"





to_json = {'total_count': 10, 'Number of ragular':0, 'Number of student':0,
           'Number of advance':0, 'Number of late':0,'Date':'12-12-2021' ,'tickets':[]}
with open('my.json', 'w') as file:
    json.dump(to_json, file, indent=3)

first = RagularTicket(1)
print(first)
second = RagularTicket(2)
print(second)
thirs = AdvanceTicket(3)
print(thirs)
forth = StudentTicket(4)
print(forth)
fifth =  LateTickets(5)
