
class Person:

    def __init__(self, fName, lName):  # accepts for first name and last name
        self.__fName = fName
        self.__lName = lName

    # Appropriate constructors and functions for data attributes

    def set_firstname(self, fName):
        self.__fName = fName

    def get_firstname(self):
        return self.__fName

    def set_lastname(self, lName):
        self.__lName = lName

    def get_lastname(self):
        return self.__lName

    def __str__(self):
        return "Name : " + self.__fName + " " + self.__lName + "\n"



