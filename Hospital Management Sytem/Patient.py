class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode,symptoms):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            postcode(string):Postal code of the patient 
        """

        #ToDo1--------------------------------------------
        self.__first_name=first_name  
        self.__surname=surname          
        self.__age=age                 
        self.__mobile=mobile        
        self.__postcode=postcode       #the undescore__ represents this is a private attribute
        self.__appointments=[]
        self.__symptoms = symptoms  # Default to an empty list if None
        self.__doctor = 'None'      #private  attribute   

        
       

    
    def full_name(self) :
        """full name is first_name and surname"""
        #ToDo2-----------------------------------------------------
        return f"{self.__first_name} {self.__surname}"     

    
    def get_surname(self):
        """Returns the surname of the patient."""
        return self.__surname 

    def get_doctor(self) :
        #ToDo3-------------------------------------------------
        return self.__doctor
    
    def set_doctor(self, doctor):
        """Assign a doctor to the patient."""
        self.__doctor = doctor


    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

       
    def get_symptoms(self):
        return self.__symptoms
    
    def set_symptoms(self,new_symptoms):
        self.__symptoms=new_symptoms


    def print_symptoms(self):
        """prints all the symptoms"""
        #ToDo4-------------------------------------
        op=input("Enter  Symptoms: ")
        print(op)
        self.set_symptoms(op)

    def get_appointment(self):
        return self.__appointments
    
    def more_appointment(self,appoint):
        self.__appointments.append(appoint)

    
    def set_symptoms(self, symptoms):
        """Updates the list of symptoms.
        Args:
            symptoms (list): List of symptoms
        """
        self.__symptoms = symptoms

    def get_symptoms(self):
        """Returns the list of symptoms."""
        return self.__symptoms

    def print_symptoms(self):
        """Prints all the symptoms."""
        op = input("Enter Symptoms: ")
        symptoms_list = [symptom.strip() for symptom in op.split(",")]
        self.set_symptoms(symptoms_list)
        print("Symptoms updated:", ", ".join(self.__symptoms))


    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}|{", ".join(self.__symptoms):^20}'


