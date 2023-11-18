
class HospitalBill:

    def __init__(self, patient, hospitalCharges, doctorFee, roomCharges):
        self.__patient = patient
        self.__hospitalCharges = hospitalCharges
        self.__doctorFee = doctorFee
        self.__roomCharges = roomCharges

    def set_patient(self, patient):
        self.__patient = patient

    def get_patient(self):
        return self.__patient

    def set_hospitalCharges(self, hospitalCharges):
        self.__hospitalCharges = hospitalCharges

    def get_hospitalCharges(self):
        return self.__hospitalCharges

    def set_doctorFee(self, doctorFee):
        self.__doctorFee = doctorFee

    def get_doctorFee(self):
        return self.__doctorFee

    def set_roomCharges(self, roomCharges):
        self.__roomCharges = roomCharges

    def get_roomCharges(self):
        return self.__roomCharges

    def totalBill(self):
        return str(self.__hospitalCharges + self.__doctorFee + self.__roomCharges)

    def __str__(self):
        output1 = "Bill of Patient \n"
        output2 = self.__patient.__str__()
        output3 = " \n Hospital Charges : $ " + str(self.__hospitalCharges)
        output4 = "\n Doctor Fee : $ " + str(self.__doctorFee)
        output5 = "\n Room Charges : $ " + str(self.__roomCharges)
        output6 = "\n -------------------- Total Billing Charges : $ " + self.totalBill() + "-------------------- \n"
        return output1 + output2 + output3 + output4 + output5 + output6





