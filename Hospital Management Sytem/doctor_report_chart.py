import matplotlib.pyplot as plt

class Doctor:
    def __init__(self, first_name, surname, specialty):
        
        self.first_name = first_name
        self.surname = surname
        self.specialty = specialty
        self.patients = []  

    def assign_patient(self, patient):
        """Assign a patient to the doctor."""
        self.patients.append(patient)

    def get_patient_count(self):
        """Return the number of patients assigned to the doctor."""
        return len(self.patients)

    def __str__(self):
        """Return a string representation of the doctor."""
        return f'{self.first_name} {self.surname} ({self.specialty})'


def plot_doctor_report(doctors):
    """
    Create and present a bar chart showing the number of patients assigned to each doctor.
    
    Args:
        doctors (list): A list of Doctor objects
    """
    # Get the data for the plot
    doctor_names = [str(doctor) for doctor in doctors] 
    patients_per_doctor = [doctor.get_patient_count() for doctor in doctors]

    # Create the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(doctor_names, patients_per_doctor, color='skyblue')

    # Add labels and title
    plt.xlabel('Doctors')
    plt.ylabel('Number of Patients')
    plt.title('Patients Assigned to Doctors')

    # Show the plot
    plt.show()

    # Close the plot after it's closed manually
    plt.close()


doctors = [
    Doctor('John', 'Smith', 'Internal Medicine'),
    Doctor('Jane', 'Doe', 'Cardiology'),
    Doctor('Alex', 'Johnson', 'Pediatrics')
]

doctors[0].assign_patient('Patient A')
doctors[0].assign_patient('Patient B')
doctors[1].assign_patient('Patient C')
doctors[2].assign_patient('Patient D')
doctors[2].assign_patient('Patient E')
doctors[2].assign_patient('Patient F')

# Now check patient counts before plotting
print(f"{doctors[0].first_name} {doctors[0].surname} has {doctors[0].get_patient_count()} patients.")
print(f"{doctors[1].first_name} {doctors[1].surname} has {doctors[1].get_patient_count()} patients.")
print(f"{doctors[2].first_name} {doctors[2].surname} has {doctors[2].get_patient_count()} patients.")

# Display the chart with updated data
plot_doctor_report(doctors) 