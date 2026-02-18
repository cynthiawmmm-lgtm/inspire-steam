# Name : Cynthia Wanjiru
# Date : 17/02/2026
# Program to format the output in different styles

name = "Cynthia Wanjiru"

weight = 60 #weight in kg

fav_team = "liverpoool"

height = 126 # height in cm

#1. format using printf(f"{}")

print(f"My name is {name} and I weigh {weight} kgs")

#2. using f string
msg = f"my name is {name} and I Support {fav_team}"
print(msg)

#3. using {} and . format()

print("my name {0} and I am {1} cms tall". format(name,height))

#4. using output specifiers %s - string

import math
print("the value of pi is approximately %5.3f."% math.pi)
print("Isupport %s"%fav_team)