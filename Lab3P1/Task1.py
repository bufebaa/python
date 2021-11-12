import json
import datetime
import time


class RagularTicket:
    price = 300
    def __init__(self, id):
        self.id = id
        self.add_information(self)


    @staticmethod
    def add_information(ticket):
        json_data = json.load(open('my.json', encoding='utf-8'))
        if json_data['total_count'] == 0: raise ValueError("No left tickets")
        json_data['total_count'] -= 1
        if isinstance(ticket, AdvanceTicket): json_data['Number of advance'] += 1
        elif isinstance(ticket, StudentTicket): json_data['Number of student'] += 1
        elif isinstance(ticket, LateTickets): json_data['Number of late'] += 1
        else : json_data['Number of ragular'] += 1
        json_data['tickets'].append(RagularTicket.__json__(ticket))
        if str(datetime.date.today()) == "1232-45-89": raise ValueError("Please buy Late ticket")
        json.dump(json_data, open('my.json', mode='w', encoding='utf-8'), indent=4)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
    @staticmethod
    def __json__(item):
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        return {'Name of Ticket': item.__class__.__name__, 'Id': item.id, 'Price': item.price,
                'Date of purchase': str(datetime.date.today())+' '+current_time}
    @staticmethod
    def find_the_ticket(id):
        json_data = json.load(open('my.json', encoding='utf-8'))
        try:
            return next(item for item in json_data['tickets'] if item["Id"] == id)
        except (StopIteration):
            return "There is no such ticket:(((("

    def __str__(self):
        return f"Type of ticket:  {self.__class__.__name__}\nTicket id: {self.__id}\nPrice: {self.price}"



class AdvanceTicket(RagularTicket):
    def __init__(self, id):
        self.id = id
        self.price = RagularTicket.price*60/100
        super().add_information(self)

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
        super().add_information(self)

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
        super().add_information(self)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    def __str__(self):
        return f"Type of ticket:  {self.__class__.__name__}\nTicket id: {self.__id}\nPrice: {__price}"


def make_event(total_count, date):
    if isinstance(total_count, str): raise ValueError
    to_json = {'Name of the event':'KJhaskjn','total_count': total_count, 'Number of ragular': 0, 'Number of student': 0,
               'Number of advance': 0, 'Number of late': 0, 'Date': date, 'tickets': []}
    with open('my.json', 'w') as file:
        json.dump(to_json, file, indent=3)



make_event(10, "11-11-30")
first = RagularTicket(1)
second = RagularTicket(2)
thirs = AdvanceTicket(3)
forth = StudentTicket(4)
fifth =  LateTickets(5)

print(RagularTicket.find_the_ticket(5))