import re
class FileManager:
    def __init__(self, file_name):
        self.__file_name=file_name
        my_file = open(file_name, "a")
        my_file.close()

    def write(self, text):
        with open(self.__file_name,"a") as text_file:
            text_file.write(text)

    def read(self):
        with open(self.__file_name, "r") as text_file:
            file_content = text_file.read()
            print(file_content)

    def count_characters(self):
        with open(self.__file_name, "r") as text_file:
            return len(text_file.read())

    def count_words(self):
        with open(self.__file_name, "rt") as text_file:
            data = text_file.read()
            return len(data.split())

    def count_lines(self):
        with open(self.__file_name, "r") as text_file:
            number_of_lines = 0
            for line in text_file:
                number_of_lines += 1
        return number_of_lines

    def count_sentences(self):
        with open(self.__file_name, "r") as text_file:
            file_content = text_file.read()
            number = len(re.split(r'[.!?]+', file_content))-1
        return number


first = FileManager("text.txt")
print(first.count_sentences())




