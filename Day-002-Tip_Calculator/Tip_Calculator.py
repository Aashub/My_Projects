
print("Welcome to the Tip Calculator")
total_bill = input("enter the total amount you have to pay $")
number_of_people = input("enter the number of how many people you are")
tip = input("enter the amount you want split into pay")

float(tip)
tip1 = 1.10
tip2 = 1.12
tip3 = 1.15
spplited_amount = 0

if tip == tip1:
 spplited_amount = (float(total_bill) / int(number_of_people)) *  float(tip1)

elif tip == tip2:
 spplited_amount = (float(total_bill) / int(number_of_people)) *  float(tip2)

else :
 spplited_amount = (float(total_bill) / int(number_of_people)) *  float(tip3)

final_amount = round(spplited_amount, 2)
final_amount = "{:.2f}".format(spplited_amount)
 

print(f"the amount is splitted between friends are $:{final_amount}")

