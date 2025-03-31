import matplotlib.pyplot as plt   



class Doctor:
    def __init__(self, first, last, spec):  # shortened param names, 
       
        self.first_name = first  
        self.last_name = last    # using last_name instead of surname 
        self.specialty = spec
        self.patients = []       # intialising empty list 
        
       
    def add_patient(self, patient):  
        """Add patient to doc's list"""  
        self.patients.append(patient)
    
    def count_patients(self):   
        return len(self.patients)
    
    def __str__(self):
        
        return f"Dr. {self.first_name} {self.last_name} - {self.specialty}"


# setting up some test doctors
my_doctors = [
    Doctor('John', 'Smith', 'Internal Med'),      
    Doctor('Jane', 'Doe', 'Cardiology'),          
    Doctor('Alex', 'Johnson', 'Peds'),            
]


my_doctors[0].add_patient('Bob Wilson')    
my_doctors[0].add_patient('Sarah Chen')
my_doctors[0].add_patient('Mike Johnson')
my_doctors[1].add_patient('Tom Baker')
my_doctors[1].add_patient('Emma Davis')
my_doctors[2].add_patient('Lucy Smith')
my_doctors[2].add_patient('Kevin Wu')
my_doctors[2].add_patient('Diana Ross')




doc_patient_counts = {str(doc): doc.count_patients() for doc in my_doctors}

plt.figure(figsize=(10, 8)) 


plt.pie(
    doc_patient_counts.values(),
    labels=doc_patient_counts.keys(),
    autopct='%.1f%%',  
    startangle=45,     
          
)

plt.title('Patient Distribution by Doctor\n(2025 Q1)')  


plt.tight_layout()
plt.show()