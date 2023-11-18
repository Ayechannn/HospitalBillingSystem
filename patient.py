
from person import Person
from doctor import Doctor


class Patient(Person):

    def __init__(self, fName, lName, ID, age, DOB, admittedDate, dischargedDate, phy):
        Person.__init__(self, fName, lName)
        self.__ID = ID
        self.__age = age
        self.__DOB = DOB
        self.__admittedDate = admittedDate
        self.__dischargedDate = dischargedDate
        if type(phy) == list:
            self.__phy = Doctor(phy[0], phy[1], phy[2])
        elif type(phy) == Doctor:
            self.__phy = phy

    def set_ID(self, ID):
        self.__ID = ID

    def get_ID(self):
        return self.__ID

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_DOB(self, DOB):
        self.__DOB = DOB

    def get_DOB(self):
        return self.__DOB

    def set_admittedDate(self, admittedDate):
        self.__admittedDate = admittedDate

    def get_admittedDate(self):
        return self.__admittedDate

    def set_dischargedDate(self, dischargedDate):
        self.__dischargedDate = dischargedDate

    def get_dischargedDate(self):
        return self.__dischargedDate

    def set_phy(self, phy):
        self.__phy = phy

    def get_phy(self):
        return self.__phy

    def __str__(self):
        output1 = super().__str__()
        output2 = "Patient ID : " + self.__ID + "\nAge : " + str(self.__age) + "\n"
        output3 = "Date of Birth : " + self.__DOB.__str__() + "\n"
        output4 = "Attending Physician's Name : " + self.__phy.get_firstname() + " " + self.__phy.get_lastname() + "\n"
        output5 = "Admission Date : " + self.__admittedDate.__str__() + "\n"
        output6 = "Discharged Date : " + self.__dischargedDate.__str__() + "\n"
        return output1 + output2 + output3 + output4 + output5 + output6









