# Name : Cynthia Wanjiru
# Date : 19/02/2026
# Program to display functions

def cook_egg():
    oil = "20ml"
    pan  = True
    fire = True 
    eggs = 2

    print(f"the pan is {pan}, and the fire is {fire},\ add {oil} amount of oil and cook {eggs} eggs")

print("here is statement 1")

print("here is statement 2")

cook_egg()

print("here is statement 3")

# Ride fare creating function

def create_fare(route,distance,is_rush_hour):

    fare = distance * 10
    if is_rush_hour == True:
        fare = fare * 1.5
    print(f"your fare to {route} is {fare}")

rush_hour = True
Returned_fare = create_fare("Juja-Allsops",7,rush_hour)
print(f"the fare returned is: {Returned_fare}")
create_fare("Juja-Allsops",7,rush_hour )

# passing a list as a parameter
def write_all_interests(interests):
    for interests in interests:
        print(f"I am interested in {interests}")

all_interests = ["swimming","hiking","reading novels"]

write_all_interests(all_interests)