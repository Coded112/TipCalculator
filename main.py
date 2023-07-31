#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("welocome to the tip calculator!!")
a = input("what was the total bill? $")
b = input("what percentage do you want to tip? 10,12 or 15:")
c = input("how many people wants to split the  bill?")
b1 = int(b) / 100 + 1
a1 = b1 + float(a)
c1 = a1 / int(c)
print(f"Enter each pearson should pay:{c1}")


