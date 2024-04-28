 # Elijah Alford
 # April/21/2024
 # P2HW1
 # Create a program that does some basic math on numbers that are entered.


budget = float(input("Enter budget:"))

destination = input("Enter your travel destination:")

gas = float(input("About how much will be spent on gas?"))

accomodation = float(input("Approximately, how much will you need for accomodation/hotel?"))

food = float(input("Last, how much do you need for food?"))

adding = int(gas)+int(accomodation)+int(food)

#Add travel exspenses together then subtract from the budget.

print("-----------Travel Expenses----------")
print("Location:         ",destination)

print(f"Initial Budget:    ${budget:.2f}")

print(f"Fuel:              ${gas:.2f}")

print(f"Accomodation:      ${accomodation:.2f}")

print(f"Food:              ${food:.2f}")

subtract= int(budget)-int(gas)-int(accomodation)-int(food)

print("-------------------------------------------")

print(f'Remaining Balance: ${subtract:.2f}')
