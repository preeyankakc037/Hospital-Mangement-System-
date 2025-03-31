import random
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


#This function handles login operations 
def handle_login():
    username = username_input.get()
    password = password_input.get()
    
    if username == 'admin' and password == '123':
        messagebox.showinfo('Login Successful', 'Login Successful')
        root.withdraw()  
        open_operations_window()  #opens the operations window
    else:
        messagebox.showerror('Login Failed', 'Incorrect username or password')


# This function open Doctor Management window
def open_doctor_management():
    doc_window = Toplevel()
    doc_window.title("Doctor Management")
    doc_window.geometry("400x300")

    Label(doc_window, text="Doctor Management", font=("Verdana", 14)).pack(pady=10)

    Button(doc_window, text="Register Doctor", width=30, command=register_doctor).pack(pady=5)
    Button(doc_window, text="View Doctors", width=30, command=view_doctors).pack(pady=5)
    Button(doc_window, text="Update Doctor", width=30, command=update_doctor).pack(pady=5)
    Button(doc_window, text="Delete Doctor", width=30, command=delete_doctor).pack(pady=5)

    Button(doc_window, text="Close", width=30, command=doc_window.destroy).pack(pady=10)


def print_option(option):
    print(f"Option selected: {option}")


# This function  open operations menu
def open_operations_window():
    op_window = Toplevel() 
    op_window.title("Operations")
    op_window.geometry("500x400")
    
    Label(op_window, text="Choose the operation:", font=("Verdana", 14)).pack(pady=10)
    
    Button(op_window, text="1- Register/View/Update/Delete Doctor", bg='#90EE90', width=40, command=open_doctor_management).pack(pady=5)
    Button(op_window, text="2- Discharge Patients", bg='#90EE90', width=40, command=discharge_patients).pack(pady=5)
    Button(op_window, text="3- View Discharged Patient", bg='#90EE90', width=40, command=view_discharged_patients).pack(pady=5)
    Button(op_window, text="4- Assign Doctor to a Patient", bg='#90EE90', width=40, command=assign_doctor_to_patient).pack(pady=5)
    Button(op_window, text="5- Relocate Doctor to a Patient", bg='#90EE90', width=40, command=relocate_doctor_to_patient).pack(pady=5)
    Button(op_window, text="6- View Management Report", bg='#90EE90', width=40, command=view_management_report).pack(pady=5)
    Button(op_window, text="7- Update Admin Details", bg='#90EE90', width=40, command=update_admin_details).pack(pady=5)
    Button(op_window, text="8- Quit", bg='#90EE90', width=40, command=op_window.destroy).pack(pady=10)
    
    op_window.configure(background='#EFEFFE')


#Registering a doctor 
def register_doctor():
    reg_window = Toplevel()
    reg_window.title("Register Doctor")
    reg_window.geometry("400x250")

    Label(reg_window, text="Enter Doctor's Details", font=("Verdana", 12)).pack(pady=10)

    Label(reg_window, text="First Name:").pack()
    first_name_entry = Entry(reg_window, width=30)
    first_name_entry.pack()

    Label(reg_window, text="Surname:").pack()
    surname_entry = Entry(reg_window, width=30)
    surname_entry.pack()

    Label(reg_window, text="Specialty:").pack()
    specialty_entry = Entry(reg_window, width=30)
    specialty_entry.pack()

    def save_doctor():
        first_name = first_name_entry.get()
        surname = surname_entry.get()
        specialty = specialty_entry.get()
        
        if first_name and surname and specialty:
            try:
                from Doctor import add_doctor  # Ensure doctor.py has add_doctor()
                add_doctor(first_name, surname, specialty)
                messagebox.showinfo("Success", f"Doctor {first_name} {surname} registered successfully!")
                reg_window.destroy()
            except ImportError:
                messagebox.showerror("Error", "Unable to import the Doctor module.")
        else:
            messagebox.showwarning("Error", "All fields are required.")

    Button(reg_window, text="Register", width=20, command=save_doctor).pack(pady=10)



def view_doctors():
    view_window = Toplevel()
    view_window.title("Doctor List")
    view_window.geometry("400x250")

    Label(view_window, text="List of Doctors", font=("Verdana", 14)).pack(pady=10)

    from Doctor import get_all_doctors  # Ensure doctor.py has get_all_doctors()

    doctors = get_all_doctors()

    if doctors:
        for doctor in doctors:
            Label(view_window, text=str(doctor), font=("Verdana", 10)).pack()
    else:
        Label(view_window, text="No Doctors Registered", font=("Verdana", 10)).pack()


def update_doctor():
    messagebox.showinfo("Update Doctor", "Functionality to be added later")


def delete_doctor():
    messagebox.showinfo("Delete Doctor", "Functionality to be added later")

def view_management_report():
    report_window = Toplevel()
    report_window.title("Hospital Management Report")
    report_window.geometry("500x400")

    Label(report_window, text="Hospital Management Report", font=("Verdana", 12)).pack(pady=10)

    # Manually defined data for the report
    total_patients = 10  
    total_doctors = 5  
    total_discharged = 3  
    total_admissions_today = 12  

    # Making a report 
    report_data = f"""
    Total Patients: {total_patients}
    Total Doctors: {total_doctors}
    Total Discharged: {total_discharged}
    Total Admissions Today: {total_admissions_today}
    """

    #Patients List 
    patients = [
        ("Daivd", "Smith", 15, "07123456789", "C1 ABC", "fever,headache"),
        ("Sara", "Smith", 20, "07012345678", "B1 234", "Nausea"),
        ("Mike", "Jones", 37, "07555551234", "L2 2AB", "Weight gain"),
        ("Daivd", "Smith", 15, "07123456789", "C1 ABC", "Vomiting"),
        ("Mohan", "Kc", 23, "347348746877", "b1 dsc", "Diziness"),
        ("Kashish", "Shenoy", 34, "344223434423", "y2 jhf", "Shoulder Pain"),
        ("Taniya", "Kc", 23, "23123", "4 242", "Fever")
    ]

    #
    discharged_patients = random.sample(patients, 3)

    # Adds discharged patients info  to the report
    report_data += "\n\nDischarged Patients:\n"
    for patient in discharged_patients:
        patient_info = f"{patient[0]} {patient[1]}, Age: {patient[2]}, Contact: {patient[3]}, Address: {patient[4]}, Symptoms: {patient[5]}"
        report_data += patient_info + "\n"

    # Displays the report 
    Label(report_window, text=report_data, font=("Verdana", 7), justify="left", wraplength=450).pack(pady=10)

    Button(report_window, text="Close", width=20, command=report_window.destroy).pack(pady=10)


def discharge_patients():
    messagebox.showinfo("Discharge Patients", "Functionality to be added later")


from tkinter import Toplevel, Label, Button

def view_discharged_patients():
    report_window = Toplevel()
    report_window.title("Discharged Patients")
    report_window.geometry("500x400")

    Label(report_window, text="Discharged Patients", font=("Verdana", 14)).pack(pady=10)

    # List of the  patients
    patients = [
        ("Daivd", "Smith", 15, "07123456789", "C1 ABC", "fever, headache"),
        ("Sara", "Smith", 20, "07012345678", "B1 234", "Nausea"),
        ("Mike", "Jones", 37, "07555551234", "L2 2AB", "Weight gain"),
        ("Daivd", "Smith", 15, "07123456789", "C1 ABC", "Vomiting"),
        ("Mohan", "Kc", 23, "347348746877", "b1 dsc", "Diziness"),
        ("Kashish", "Shenoy", 34, "344223434423", "y2 jhf", "Shoulder Pain"),
        ("Taniya", "Kc", 23, "23123", "4 242", "Fever")
    ]

    
    discharged_patients = [
        patients[0],  
        patients[3],  
        patients[6]   
    ]

    discharged_text = "The following patients have been discharged:\n\n"
    for patient in discharged_patients:
        patient_info = f"{patient[0]} {patient[1]}, Age: {patient[2]}, Contact: {patient[3]}, Address: {patient[4]}, Symptoms: {patient[5]}"
        discharged_text += patient_info + "\n"

    Label(report_window, text=discharged_text, font=("Verdana", 12), justify="left", wraplength=450).pack(pady=10)

    Button(report_window, text="Close", width=20, command=report_window.destroy).pack(pady=10)




def assign_doctor_to_patient():
    messagebox.showinfo("Assign Doctor to a Patient", "Functionality to be added later")


def relocate_doctor_to_patient():
    messagebox.showinfo("Relocate Doctor to a Patient", "Functionality to be added later")


def update_admin_details():
    messagebox.showinfo("Update Admin Details", "Functionality to be added later")


# main login window
root = Tk()
root.title("Login")  

# Importing the absoulte path of image 
import os
icon_path = r"C:\Users\ASUS\Desktop\PartB System_Development\user-regular.ico"

if os.path.exists(icon_path):
    root.iconbitmap(icon_path)
else:
    print("Warning: Icon file not found. Check the file path.")


root.geometry('600x500')
root.configure(background='#EFEFFE')


# ----------------------------------------------------------

# Load image with error handling
image_path = r"C:\Users\ASUS\Desktop\PartB System_Development\Medicare.jpg"

if os.path.exists(image_path):
    img = ImageTk.PhotoImage(Image.open(image_path).resize((90, 70)))
    img_label = Label(root, image=img)
    img_label.pack()
else:
    print("Error: Medicare.jpg not found.")




text_Label = Label(root, text='Hospital Management System', fg="green", bg="#EFEFFE")
text_Label.pack()
text_Label.config(font=('Verdana', 24))

# Username input
username_Label = Label(root, text="Enter Username", bg='#EFEFFE')
username_Label.pack(pady=(20, 5))
username_Label.config(font=('Verdana', 12))

username_input = Entry(root, width=35)
username_input.pack(ipady=6, pady=(1, 15))

# Password input
password_Label = Label(root, text="Enter password", bg='#EFEFFE')
password_Label.pack(pady=(20, 5))
password_Label.config(font=('Verdana', 12))

password_input = Entry(root, width=35, show="*")
password_input.pack(ipady=6, pady=(1, 15))

# Password Visibility
def toggle_password():
    if password_input.cget('show') == '*':
        password_input.config(show='')  
        toggle_btn.config(text="Hide")
    else:
        password_input.config(show='*')  
        toggle_btn.config(text="Show")

toggle_btn = Button(root, text="Show", command=toggle_password)
toggle_btn.pack(pady=5)

# Login Button
login_btn = Button(root, text="Login Here", bg='white', fg='black', width=14, height=2, command=handle_login)
login_btn.pack(pady=(10, 20))
login_btn.config(font=('Verdana', 13))

root.mainloop()  # Keeps the GUI running
