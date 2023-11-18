
from person import Person


class Doctor(Person):

    def __init__(self, fName, lName, specialization):
        Person.__init__(self, fName, lName)
        self.__specialization = specialization

    # Methods for data attributes

    def set_specialization(self, specialization):
        self.__specialization = specialization

    def get_specialization(self):
        return self.__specialization

    def __str__(self):
        output1 = super().__str__()
        output2 = "Specialized in : " + self.__specialization + "\n"
        return output1 + output2



