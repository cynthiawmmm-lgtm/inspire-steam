# Name : Cynthia Wanjiru
# Date : 11/02/2026
# Program to calculate geometric progression

# calculating the nth term

a = int(input("enter the first number: "))
n = int(input("enter the number of terms:"))
r = int(input("enter the ratio difference:"))

nth_term = a*(r**(n-1))
Sn=a*(1-r**n)/(1-r)

print(f"the nth term")