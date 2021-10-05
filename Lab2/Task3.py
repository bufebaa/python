from math import ceil, floor
class Group:
    number_of_students = 0
    def __new__(cls, *students):
        if cls.number_of_students > 20:
            print("Group if full")
            raise SystemExit(1)
        return super(Group, cls).__new__(cls)

    def __init__(self, *students):
        self.students = students
        self.students = sorted(self.students, key = sort_key, reverse=True)

    def __str__(self):
        output = 'Top five: \n'
        count = 1
        for i in self.students:
            if count <= 5:
                output += i.name +" "+ str(i.total_score)+'\n'
                count += 1
        return output


class Student(Group):
    names = list()
    def __new__(cls, full_name, record_b_n, **grades):
        if full_name in cls.names:
            print("New student cant be added, there is persone with a same name: "+full_name)
            raise SystemExit(1)
        else:
            cls.names.append(full_name)
        return super(Student, cls).__new__(cls)

    def __init__(self, full_name, record_b_n, **grades):
        if not isinstance(full_name, str): raise TypeError
        self.name = full_name
        self.record_b_n = record_b_n
        self.grades = grades
        self.avarge_v()

    def avarge_v(self):
        total_score = 0
        for i in self.grades.values():
            total_score += i
        self.total_score = round(total_score/len(self.grades), 4)


def sort_key(t):
    return t.total_score


first = Student('Fredric ko', 'skd', math = 58, kewj = 78, iasdj=21)
second = Student('Sam Smith', 'skad', math =90, fdjn=98, sdch=98)
third = Student('asdklm sa', 'sas', math = 66, kewj = 44, iasdj=32)
fivth = Student('Dasha K', 'skd', math = 58, kewj = 78, iasdj=21)
six = Student('Liza Goncharova', 'skad', math =1, fdjn=1, sdch=100)
seven = Student('Paul P', 'sas', math = 88, kewj = 11, iasdj=65)
eight = Student('Have fun', 'skd', math = 85, kewj = 0, iasdj=89)
nine = Student('Telephone g', 'skad', math =78, fdjn=22, sdch=9)
ten = Student('Computer d', 'sas', math = 2, kewj = 5, iasdj=3)
eleven = Student('Fredric ko', 'skd', math = 58, kewj = 78, iasdj=21)


first_g = Group(first, second, third, fivth, six, seven, eight, nine, ten, eleven)
print(first_g)

