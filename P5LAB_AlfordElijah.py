import random


def disperse_change(total_change):
   if total_change <= 0:
      print('No change')
      return
    
   dollar = total_change//100
   cents = total_change%100

   quarter = cents//25
   cents = cents%25

   dime = cents // 10
   cents = cents%10           

   nickel = cents // 5
   cents = cents%5            

   penny = cents // 1

#print if and elif statements to display change amount.


   if total_change == 0:
      print('No change')


   if dollar == 1:
       print(dollar, "Dollar")
   elif dollar > 0:
       print(dollar, "Dollars")

   if quarter == 1:
       print(quarter, "Quarter")
   elif quarter > 0:
       print(quarter, "Quarters")

   if dime == 1:
       print(dime, "Dime")
   elif dime > 0:
       print(dime, "Dimes")

   if nickel == 1:
       print(nickel, "Nickel")
   elif nickel > 0:
       print(nickel, "Nickels")

   if penny == 1:
       print(penny, "Penny")
   elif penny > 0:
       print(penny, "Pennies")



    

def main():

   amount_owed = round(random.uniform(0.01, 100.00), 2)
   print("You owe",amount_owed)

   
   cash = int(input("How much cash will you put in the self-checkout? "))

   change = cash - amount_owed
   print(f"Change is ${change:.2f}")

   disperse_change(change)

    

if __name__ == "__main__":
   main()
