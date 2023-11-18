from datetype import DateType
from doctor import Doctor
from hospitalbill import HospitalBill
from patient import Patient


def date_collection(placeholder):
    # Generate Date function
    print("Enter Date in the format of (Day - Month - Year)")
    entry_date = input(" Enter Patient's " + placeholder + " in DD - MM - YYYY")
    day, month, year = map(int, entry_date.split('-'))
    return DateType(day, month, year)


def create_patient_info():
    # Get Patient information
    # function for patient data
    print("Enter Patient Detail Information")
    patient_id = input("Enter Patient ID : ")
    patient_firstname = input("Enter Patient's first name : ")
    patient_lastname = input("Enter Patient's last name : ")
    patient_age = input("Enter Patient's age : ")
    patient_dob = date_collection(" Date of Birth : ")
    patient_admitted_date = date_collection(" Patient's Admitted Date : ")
    patient_discharged_date = date_collection(" Patient's Discharged Date : ")
    return [patient_firstname, patient_lastname, patient_id, patient_age, patient_dob, patient_admitted_date,
            patient_discharged_date]


def create_doctor_info():
    # Get Doctor information
    print("Enter Doctor Detail Information")
    doctor_firstname = input(" Enter Doctor's first name : ")
    doctor_lastname = input(" Enter Doctor's last name : ")
    doctor_speciality = input(" Enter Doctor's Speciality : ")
    add_doctor = Doctor(doctor_firstname, doctor_lastname, doctor_speciality)
    return add_doctor


def create_hospital_bill(patient):
    print(" Enter Patient ID for the detail information of Hospital Bill : " + patient.get_ID())
    hospital = float(input(" Enter Hospital Charges : "))
    doctor = float(input(" Enter Doctor Fee : "))
    room = float(input(" Enter Room Charges : "))
    add_bill = HospitalBill(patient, hospital, doctor, room)
    return add_bill


# Function for reading detail information from a csv file and creating a list of patients
def createPatientList():
    patients = []
    file = open('patientData.csv', "r")
    for line in file:
        data = line.rstrip().split(",")
        new_patient = Patient(data[0], data[1], data[2], data[3], [data[4], data[5], data[6]],
                              [data[7], data[8], data[9]], [data[10], data[11], data[12]],
                              [data[13], data[14], data[15]])
        patients.append(new_patient)
    file.close()
    return patients


# Function for reading detail information from a csv file and creating a list of doctors
def createDoctorList():
    doctors = []
    file = open('doctorData.csv', "r")
    for line in file:
        data = line.rstrip().split(",")
        new_doctor = Doctor(data[0], data[1], data[2])
        doctors.append(new_doctor)
    file.close()
    return doctors


# Main function
def main():
    answer = True
    bill = None
    patient_list = None
    doctor_list = None
    while answer:
        print(" The Billing System of the Hospital ")
        print("""
        1. Enter the Detail Information of the Patient
        2. Print the Hospital Bill of the Patient
        3. Create Patient List
        4. Create Doctor List
        5. View Patient List
        6. View Doctor List
        7. Exit
        """)

        answer = input(" Choose an option ")
        print()

        if answer == "1":
            patient_info = create_patient_info()
            print()
            add_doctor = create_doctor_info()
            patient = Patient(patient_info[0], patient_info[1], patient_info[2], patient_info[3],
                              patient_info[4], patient_info[5], patient_info[6], add_doctor)

            print()
            print("\n The creation of the Patient is successful now. \n")
            bill = create_hospital_bill(patient)
            print(" \n The Hospital Bill for the Patient is successful now. \n")

        elif answer == "2":
            if bill:
                print(bill)
            else:
                print(" The data of the patient must be entered first. Go to Option 1!")

        elif answer == "3":
            patient_list = createPatientList()
            print(" The list creation of the patient is successful.")

        elif answer == "4":
            doctor_list = createDoctorList()
            print(" The list creation of the doctor is successful.")

        elif answer == "5":
            if patient_list:
                print(" The List of the Patients ")
                for j in range(len(patient_list)):
                    print("Patient ", j+1)
                    print(patient_list[j])
            else:
                print(" The list of the patient must be created first. Go to Option 3!")

        elif answer == "6":
            if doctor_list:
                print(" The List of the Doctors ")
                for j in range(len(doctor_list)):
                    print("Doctor ", j+1)
                    print(doctor_list[j])
            else:
                print(" The list of the Doctor must be created first. Go to Option 4!")

        elif answer == "7":
            print(" \n Program Exit \n")
            answer = False

        else:
            print(" \n The choice is invalid. Please try again.")

        print()

# Call the main function
main()













