# Name : Cynthia Wanjiru
# Date : 16/02/2026
# Program to calculate income tax

salary = int(input("enter your gross salary"))

if salary < 45000:
    tax =( 0.05 * salary) / 100
    net_salary = salary - tax

print(f"gross salary = {salary}") 
print(f"Net salary = {net_salary}")    
print(f"tax = {tax}")

elif salary>50000 and salary<100000:
    tax=(0.05*salary)100
    net_salary = salary - tax

print(f"gross salary = {salary}") 
print(f"Net salary = {net_salary}")    
print(f"tax = {tax}")

elif salary>100000:
    tax =(2.5*salary)/100
     net_salary = salary - tax

print(f"gross salary = {salary}") 
print(f"Net salary = {net_salary}")    
print(f"tax = {tax}")