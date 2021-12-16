import pymysql
from CONFIG import  host, user, password, db_name
from interface import ICourse, ILocalCourse, IOffsiteCourse, ICourseFactory, ITeacher


# Сlass for Teacher's initialization and showing information about him
class Teacher(ITeacher):

    #Teacher's initialization
    def __init__(self, name):
        self.name = name
        self.course = None

    @property
    def name(self):
        return  self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        if name == " ":
            raise  TypeError
        self.__name = name

    #Str method for teacher
    def __str__(self):
        return f'{self.name}: {self.course.name}'



# Base class for Courses initialization and showing information about them
class Course(ICourse):

    #Course initialization
    def __init__(self, name, teacher, lessons):
        self.name = name
        self.teacher = teacher
        self.lessons = lessons

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or name == " ":
            raise TypeError
        self.__name = name

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, name):
        if not isinstance(name, Teacher) :
            raise TypeError
        self.__teacher = name
    #Str method for teacher
    def __str__(self):
        return f'Corse name: {self.name}\nTeachers name: {self.__teacher.name}' \
                f'\nLessons: {self.lessons}'



# Class for LocalCourse initialization
class LocalCourse(Course, ILocalCourse):

    def __init__(self, name, teacher, lessons):
        super().__init__(name, teacher, lessons)
        self.type = "Local"

    def __str__(self):
        return super().__str__() + f"\nType: {self.type}"


# Class for OffsiteCourse initialization
class OffsiteCourse(Course,IOffsiteCourse):

    def __init__(self, name, teacher, lessons):
        super().__init__(name, teacher, lessons)
        self.type = "Offsite"

    def __str__(self):
        return super().__str__() + f"\nType: {self.type}"


# Class for Courses creation, adding info to database, showinf info from it
class CourseFactory(ICourseFactory):

    # Method which create connection to db
    def create_connection(self):
        try:
            connection = pymysql.connect(
                host = host,
                port = 3307,
                user = user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            return connection
        except Exception as ex:
            raise ValueError

        return connection

    # Method that insert info into db and create instance of Course class
    def create(self, name, teacher, lessons, type):
        if not isinstance(teacher, Teacher):
            raise ValueError

        connection = self.create_connection()
        with connection.cursor() as cursor:
            insert_data = "INSERT INTO `course` (Name, Teachers_name, Course_type, Lessons_name)" \
                           "VALUES (%s, %s, %s, %s)"
            val = [name, teacher.name, lessons, type]
            cursor.execute(insert_data, val)
            connection.commit()
        connection.close()
        if type == 'Local':
            return LocalCourse(name, teacher, lessons)
        elif type == "Offset":
             return OffsiteCourse(name, teacher, type)

    # Method that show info from db about Teacher and course
    def show_info(self, teacher):
        if not isinstance(teacher, Teacher):
            raise ValueError
        connection = self.create_connection()
        with connection.cursor() as cursor:
            select_info = "SELECT  Teachers_name, Name, Course_type, Lessons_name " \
                         "FROM `course`" \
                         "WHERE Teachers_name = %s"
            val = [teacher.name]
            cursor.execute(select_info, val)
            rows = cursor.fetchall()
            if rows == "":
                print("Nothing found")
            else:
                for row in rows:
                    print(row)
        connection.close()

    # Delete course from db
    def delete_course(self, course_name):
        if isinstance(course_name, str):
            raise TypeError

        connection = self.create_connection()
        with connection.cursor() as cursor:
            delete_course = "DELETE FROM  `course` WHERE' Name = %s"
            val = [course_name]
            try:
                cursor.execute(delete_course, val)
            except:
                print("No such course")
            connection.commit()
        connection.close()


if __name__ == '__main__':

    teacher1 = Teacher("Gragham Itter")
    course1 = CourseFactory()
    # course1.create("Math", teacher1, "Георгафия, математика, англ", 'Local')
    course1.show_info(teacher1)
