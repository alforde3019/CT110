 # Elijah Alford
 # April/14/2024
 # P1HW2
 # Create a program that does some basic math on numbers that are entered.


budget = int(input("Enter budget:"))

destination = input("Enter your travel destination:")

gas = int(input("About how much will be spent on gas?"))

accomodation = int(input("Approximately, how much will you need for accomodation/hotel?"))

food = int(input("Last, how much do you need for food?"))

adding = int(gas)+int(accomodation)+int(food)

#Add travel exspenses together then subtract from the budget.

print("-----------Travel Expenses----------")
print("Location:",destination)
print("Initial Budget:",budget)

print("Fuel:",gas)

print("Accomodation:",accomodation)

print("Food:",food)
subtract= int(budget)-int(gas)-int(accomodation)-int(food)

print(f'Remaining Balance:${subtract:.2f}')
