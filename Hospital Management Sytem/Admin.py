from Doctor import Doctor


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address



    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
            useful for displaying list of doctors, patients
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}') #:3 repesent it takes at least 3 spaces before printing item 

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        #ToDo1-------------------------------------------------------------
        if username == self.__username and password == self.__password:
            print("Login Successful")
            return username
        else:
            print("Invalid username or password. Try again.")
        return False 
    
    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2--------------------------------------------------------------
        first_name=input("Enter the First Name of the doctor: ")
        surname=input("Enter the surname of the doctor: ")
        speciality=input("Enter the speciality of the doctor: ")

        return first_name,surname,speciality

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3-----------------------------------------------
        op = input("Input: ") 


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4--------------------------------------------------------
            first_name,surname,speciality = self.get_doctor_details()  #tuple unpacking

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    name_exists=True  
                    break #ToDo5------------------------------------------
                        # save time and end the loop

            #ToDo6----------------------------------------
            if name_exists==False:
                if first_name.strip()=="" or  surname.strip()=="" or speciality.strip()=="":
                    print("Doctor's details cannot be empty. please try again!")
                else:
                    new_doctor=Doctor(first_name,surname,speciality)
                    doctors.append(new_doctor)
                # add the doctor ...
                                                         # ... to the list of doctors
            print('Doctor registered Successfuly.')
            return doctors

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7----------------------------------------------------------------
            print("ID |          Full name           |  Speciality")
            self.view(doctors) 


        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        
                        

                except ValueError: 
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: ')) # make the user input lowercase

            #ToDo8------------------------------------------------------------
            if op == 1:
                new_first_name = input("Enter the new first name: ")
                doctors[index].set_first_name(new_first_name)
            elif op == 2:
                new_surname = input("Enter the new surname: ")
                doctors[index].set_surname(new_surname)
            elif op == 3:
                new_speciality = input("Enter the new specialty: ")
                doctors[index].set_speciality(new_speciality)
            else:
                print("Invalid option. No changes made.")

            print("Doctor's details updated successfully!")

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = input('Enter the ID of the doctor to be deleted: ')
            #ToDo9-------------------------------------------------------
            try:
                index = int(doctor_index) - 1
                # if self.find_index(index, doctors):
                if 0 <= index < len(doctors):
                    del doctors[index]
                    print("Doctor deleted successfully!")
                else:
                    print("The ID Entered is Invalid. No doctor deleted.")
            except ValueError:
                print("Invalid input. Try again with a  valid doctor ID.")


           
         

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients(Grouped by Family)-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode  | Symptoms')
        #ToDo10----------------------------------------
        if patients:
            self.view(patients)
        else:
            print("No patients registered yet.")

          
  
    def same_family(self,patient):

        dict = {}
        for i in patient:
            last_name = i.get_surname()
            if last_name not in dict:
                dict[last_name] = [i]
            else:
                patient_list = dict[last_name]
                patient_list.append(i)
                dict[last_name] = patient_list

        grouped_patients = []
        for j, patient_data in dict.items():
            grouped_patients.extend(patient_data)

        return grouped_patients

    


    def relocate(self,patients,doctors):
        patients = [i for i in patients if i.get_doctor() != 'None']

        if len(patients) == 0:
            print("No patient assigned to any doctors. Assign a doctor to a patient.")
            return
        else:
            print("---Relocate a patient from one doctor to another---")

            print("-----Patients-----")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            self.view(patients)

            index = input('Please enter the patient ID: ')
            patient_index = index

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        

        try:
            doctor_index = int(input('Please enter the doctor ID: '))
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index].full_name())
                #ToDo11
                
                print('The patient is now relocated to a new doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients(Grouped by Family)----------")
        print('ID |          Full Name           |      Doctors Full Name      | Age |    Mobile     | Postcode | Symptoms')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID minus one (-1)
            patient_index = int(patient_index) - 1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return  # stop the procedures

        except ValueError:  # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return  # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms()  # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID minus one (-1)
            doctor_index = int(doctor_index) - 1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index, doctors):
                # link the patients to the doctor and vice versa
                patients[patient_index].link(doctors[doctor_index].full_name())  # Use link() instead of set_doctor()
                doctors[doctor_index].add_patient(patients[patient_index].full_name())

                print('The patient is now assigned to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError:  # the entered id could not be changed into an int
            print('The id entered is incorrect')



    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")

        patient_index = input('Please enter the patient ID: ')

        #ToDo12------------------------------------------
        try:
            index = int(patient_index) - 1
            if index in range(len(patients)):
                discharge_patients.append(patients.pop(index))
                print("Patient discharged successfully!")
            else:
                print("Invalid patient ID.")
        except ValueError:
            print("Invalid input. Please enter a valid patient ID.")


    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode | Symptoms')
        #ToDo13----------------------------------------------------------------
        if discharged_patients:
            self.view(discharged_patients)
        else:
            print("No patients have been discharged yet.")

    def management_report(self,patients,doctors):
        # Variable Initalization
        num_doctors = len(doctors)
        num_patients = len(patients)
        patients_per_doctor = {}
        appts_per_doctor = {}
        illness_counts = {}

        #Calculation 
        for doctor in doctors:
            doctor_name = doctor.full_name()
            patients_per_doctor[doctor_name] = 0
            appts_per_doctor[doctor_name] = 0
            for patient in patients:
                if patient.get_doctor() == doctor_name:
                    patients_per_doctor[doctor_name] += 1
                    appts_per_doctor[doctor_name] += len(patient.get_appointment())

        for patient in patients:
            for symptom in patient.get_symptoms():
                if symptom not in illness_counts:
                    illness_counts[symptom] = 1
                else:
                    illness_counts[symptom] += 1

        # Print the report
        print("\n---Management Report---\n")
        print(f"{'Total number of doctors':<50} : {num_doctors}")
        print(f"{'Total number of patients':<50} : {num_patients}")
        for doctor_name, num_patients in patients_per_doctor.items():
            print(f"{'Total number of patients per doctor':<50} : {doctor_name:<15} : {num_patients:>3} patients")
        for doctor_name, num_appts in appts_per_doctor.items():
            print(f"{'Total number of appointments per month per doctor':<50} : {doctor_name:<15} : {num_appts:>3} appointments")
        for symptom, num_patients in illness_counts.items():
            print(f"{'Total number of patients based on the illness':<50} : {symptom:<15} : {num_patients:>3} patients\n")
  
    
    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        try:
            op = int(input('Input: '))

            if op == 1:
            #ToDo14--------------------------------------------------------
                new_username = input("Enter the new username: ")
                self.__username = new_username
                print("Username updated successfully!")

            elif op == 2:
                password = input('Enter the new password: ')
                # validate the password
                if password == input('Enter the new password again: '):
                    self.__password = password

            elif op == 3:
                #ToDo15-----------------------------------------------
                    new_address = input("Enter the new address: ")
                    self.__address = new_address
                    print("Address updated successfully!")


            else:
                #ToDo16-------------------------------------------------
                print("Invalid option selected. No changes made.")
        except:
            print("Error occured due to wrong input")

