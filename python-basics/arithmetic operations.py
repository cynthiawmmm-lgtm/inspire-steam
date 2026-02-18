# Name : Cynthia Wanjiru
# Date : 17/02/2026
# Program to perform arithmetic operations 

f_number = 23 #first number
s_number = 45 # second number
sum_number =f_number + s_number
difference = f_number - s_number
product_number = f_number * s_number
quotient_number = f_number/s_number

print("sum of the numbers %d"%sum_number)
print("quotient of the numbers %0.2f"%quotient_number)

#modulus - remainder
print(5%4)

#even and odd numbers
for x in range (0,20):
    if (x%2 == 1):
        print("{x} is odd number")
    elif (x%2 == 0):
        print("{x} is even number")   
   print(x) 