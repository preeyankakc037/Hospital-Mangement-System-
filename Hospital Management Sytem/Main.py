# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient




def patient_file(file_container):
    try:
        file_path = "C:/Users/ASUS/Desktop/HMSPriyankaKhatri_25123827/FIles/patients.txt"  #Use the absolute path
        file = open(file_path, "r")
        list_a = []
        for i, lines in enumerate(file):
            if lines.strip():
                data = lines.split(",")
                data = [line.strip() for line in data]
                symptoms = data[5].split(",")  
                symptoms = [symptom.strip() for symptom in symptoms]  
                list_a.append(Patient(data[0], data[1], int(data[2]), data[3], data[4], symptoms))

        file.close()
        return list_a if list_a else []
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
 
    #why returning an empty list cause this function is supposed to return a list, by returining an empty list 
    #this will ensure the whole program will run without any error and always prefredd to return list rather than a none type 


def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin', '123', 'B1 1AB')  # username is 'admin', password is '123'
    doctors = [Doctor('John', 'Smith', 'Internal Med.'),
               Doctor('Jone', 'Smith', 'Pediatrics'),
               Doctor('Jone', 'Carlos', 'Cardiology')]

    
    patients=patient_file("patients.txt")
    patients=admin.same_family(patients)

    discharged_patients = []

    

    # keep trying to login till the login details are correct
    while True:
        if admin.login():
            running = True 
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Relocating doctor to a patient')
        print(' 6- view management report')
        print(' 7- Update admin detais')
        print(' 8- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register
         #ToDo1--------------------------------
          admin.doctor_management(doctors)

        elif op == '2':
            # 2- View or discharge patients
            #ToDo2------------------------------
            admin.view_patient(patients)

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    #ToDo3----------------------------
                    admin.discharge(patients, discharged_patients)

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            # 3 - view discharged patients
            #ToDo4---------------------------------------
            admin.view_discharge(discharged_patients)

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op =="5":
            #5 Relocate  a patient from one doctor to another
            admin.relocate(patients,doctors)

        elif op=="6":
            #For Displaying the Management Report
            admin.management_report(patients,doctors)

        elif op == '7':
            # 7- Update admin detais
            admin.update_details()

        elif op == '8':
            # 8 - Quit
            #ToDo5-------------------------------------------
            print("Exiting the program...")
            running = False  # Stop the program

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()












