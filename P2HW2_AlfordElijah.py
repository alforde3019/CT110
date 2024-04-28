# Elijah Alford
# April/21/2024
# P2HW2
# Ask user to enter grade for each module.


module_1 = float(input("Enter grade for Module 1: "))
module_2 = float(input("Enter grade for Module 2: "))
module_3 = float(input("Enter grade for Module 3: "))
module_4 = float(input("Enter grade for Module 4: "))
module_5 = float(input("Enter grade for Module 5: "))
module_6 = float(input("Enter grade for Module 6: "))

#Display highest,lowest,sum,and average of grades.

modules = [module_1, module_2, module_3, module_4, module_5, module_6]
print("-----------Results----------")
lowest_grade = min(modules)
print("Lowest Grade:",lowest_grade)

highest_grade = max(modules)
print("Highest Grade:",highest_grade)

all_grades = sum(modules)
print("Sum of Grades:", all_grades)

average = sum(modules)/len(modules)
print(f"Average:{average: .2f}")
print("---------------------------------")
