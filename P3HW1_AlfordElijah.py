# Elijah Alford
# April/26/2024
# P3HW1



# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = input('Enter grade for Module 1: ')
mod_2 = input('Enter grade for Module 2: ')
mod_3 = input('Enter grade for Module 3: ')
mod_4 = input('Enter grade for Module 4: ')
mod_5 = input('Enter grade for Module 5: ')
mod_6 = input('Enter grade for Module 6: ')

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5]

# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
avg= sum(grades)/len(grades)

# determine letter grade for average


if avg >= 90:
    print('Your grade is: A')

else:
    
    if average >= 80:
        print('Your grade is: B')
    else:
        print('Your grade is: F') # TO DO: finish this
        
    
    





