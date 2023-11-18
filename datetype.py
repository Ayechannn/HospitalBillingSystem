
class DateType:

    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def set_day(self, day):
        self.__day = day

    def get_day(self):
        return self.__day

    def set_month(self, month):
        self.__month = month

    def get_month(self):
        return self.__month

    def set_year(self, year):
        self.__year = year

    def get_year(self):
        return self.__year

    def __str__(self):
        return str(self.__day) + " / " + str(self.__month) + " / " + str(self.__year) + "\n"




