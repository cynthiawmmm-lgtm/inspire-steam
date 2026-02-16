# Name : Cynthia Wanjiru
# Date : 16/02/2026
# Program to calculate the factorials of numbers

number = int(input("enter the number x:"))
factorial = 1 # initialize factorial as 1
for x in range(1,number + 1):
    factorial *=x
    number=number-1

print(f"{number}! = {factorial}")