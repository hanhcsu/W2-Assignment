#Write a program that calculates the total amount of a meal purchased at a restaurant:
#Ask the user to enter the charge for the food:
FoodCharge = float(input("Please enter the charge for the food: "))

#Calculate the amounts with an 18 percent tip:
Tip = FoodCharge * 0.18
#Calculate 7 percent sales tax:
Tax = FoodCharge * 0.07
#Calculate total price:
Total = FoodCharge + Tip + Tax
#Display each of these amounts and the total price:

print(f"Food charge: ${FoodCharge:.2f}")
print(f"Tip 18%: ${Tip:.2f}")
print(f"Tax 7%: ${Tax:.2f}")
print(f"Total price is: ${Total:.2f}")