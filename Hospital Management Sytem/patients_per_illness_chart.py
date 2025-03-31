import matplotlib.pyplot as plt
from collections import Counter


patients = [
    ("Daivd", "Smith", 15, "07123456789", "C1 ABC", ["Fever", "Headache"]),
    ("Sara", "Smith", 20, "07012345678", "B1 234", ["Nausea"]),
    ("Mike", "Jones", 37, "07555551234", "L2 2AB", ["Weight Gain"]),
    ("Daivd", "Smith", 15, "07123456789", "C1 ABC", ["Vomiting"]),
    ("Mohan", "Kc", 23, "347348746877", "B1 DSC", ["Dizziness"]),
    ("Kashish", "Shenoy", 34, "344223434423", "Y2 JHF", ["Shoulder Pain"]),
    ("Taniya", "Kc", 23, "23123", "4 242", ["Fever"]),
    ("John", "Doe", 30, "1234567890", "X1 YZ1", ["Headache"]),
    ("Alice", "Brown", 28, "9876543210", "X2 YZ2", ["Headache"]),
    ("Eve", "Johnson", 35, "5555555555", "A3 BC3", ["Dizziness"]),
    ("Bob", "Taylor", 40, "7777777777", "B4 CD4", ["Dizziness"]),
    ("Charlie", "Wilson", 50, "9999999999", "C5 DE5", ["Dizziness"]),
    ("Emma", "Davis", 45, "2222222222", "D6 EF6", ["Dizziness"])
]

all_symptoms = []
for patient in patients:
    all_symptoms.extend(patient[5])  

#Count how many times a disease is repeated
illness_counts = Counter(all_symptoms)

# Extract labels and values for plotting
illnesses = list(illness_counts.keys())
counts = list(illness_counts.values())


colors = plt.cm.get_cmap("tab10", len(illnesses)).colors  # Generates distinct colors

plt.figure(figsize=(10, 5))  

# Plot bar chart
bars = plt.bar(illnesses, counts, color=colors, edgecolor='black')

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.2, str(height), 
             ha='center', fontsize=10, fontweight='bold', color='black')

#Label and Titles 
plt.xlabel("illness Type", fontsize=12, labelpad=8)
plt.ylabel("Total Number of Patients", fontsize=12, labelpad=8)
plt.title("Total Patients by illness Type", fontsize=14, fontweight='bold')

# Set X-axis labels fully horizontal (0°) for better visibility
plt.xticks(rotation=0, fontsize=10, ha='center') 
plt.yticks(fontsize=10)

# Adding Grids lines 
plt.grid(axis='y', linestyle='--', alpha=0.5)  

# Finally showing plot 
plt.show()
