#asking your to enter amount of goods

amount_purchase = float(input("Enter amount: "))
Quantity = int(input("Enter Quantity of goods:" ))

#Calculating for total amount
Total_amount = amount_purchase * Quantity
 
 #control flow



if Total_amount >= 100:
    discount = 0.1
elif Total_amount >= 50:
    discount = 0.5
else:
    discount = 0
 
final_amount = Total_amount * (1 - discount)

print("The final price after discount is $" + str(final_amount))

 