class Doctor:
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """

        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []

    
    def full_name(self) :
        #ToDo1----------------------------------------------------------------------
          """Returns the full name of the doctor"""
          return f'{self.__first_name} {self.__surname}'

    def get_first_name(self) :
        #ToDo2---------------------------------------------
        """Returns the first name of the doctor"""
        return self.__first_name

    def set_first_name(self, new_first_name):
        #ToDo3----------------------------------------------
        """Sets a new first name for the doctor"""
        self.__first_name = new_first_name

    def get_surname(self) :
        #ToDo4----------------------------------------------
        """Returns the surname of the doctor"""
        return self.__surname

    def set_surname(self, new_surname):
        #ToDo5----------------------------------------------
        """Sets a new surname for the doctor"""
        self.__surname = new_surname

    def get_speciality(self) :
        #ToDo6----------------------------------------------
        """Returns the speciality of the doctor"""
        return self.__speciality

    def set_speciality(self, new_speciality):
        #ToDo7---------------------------------------------
        """Sets a new speciality for the doctor"""
        self.__speciality = new_speciality

    def add_patient(self, patient):
        self.__patients.append(patient) 
        #  """Adds a patient to the doctor's list of patients"""

    def get_patients(self) -> list:
        return self.__patients if self.__patients else []

    def add_appointment(self, appointment):
        """Adds an appointment to the doctor's schedule"""
        self.__appointments.append(appointment)

    def get_appointments(self):
        """Returns the list of appointments"""
        return self.__appointments
    

    def __str__(self) :
     return f'{self.full_name():^30}|{self.__speciality:^15}'
   
  #Code added for GUI(TKINTER)
  # Doctor.py
    doctors_list = []

   # Doctor.py
doctors_list = []  
def add_doctor(first_name, surname, specialty):
    doctor = {
        "first_name": first_name,
        "surname": surname,
        "specialty": specialty
    }
    doctors_list.append(doctor)

def get_all_doctors():
    return doctors_list


#
# :^30 → Centers the text within 30 spaces.
# | → Separates columns like a table.