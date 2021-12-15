from abc import ABC, abstractmethod

class ICourse(ABC):

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    @name.setter
    @abstractmethod
    def name(self, name):
        raise NotImplementedError

    @property
    @abstractmethod
    def teacher(self):
        raise NotImplementedError

    @teacher.setter
    @abstractmethod
    def teacher(self, name):
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class ITeacher(ABC):

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    @name.setter
    @abstractmethod
    def name(self, name):
        raise NotImplementedError


    @abstractmethod
    def __str__(self):
        raise NotImplementedError

class ILocalCourse(ABC):

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class IOffsiteCourse(ABC):

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

class ICourseFactory(ABC):

    @abstractmethod
    def create_connection(self):
        raise NotImplementedError

    @abstractmethod
    def create(self, name, teacher, lessons, type):
        raise NotImplementedError

    @abstractmethod
    def show_info(self, teacher):
        raise NotImplementedError

    @abstractmethod
    def delete_course(self, course_name):
        raise NotImplementedError

