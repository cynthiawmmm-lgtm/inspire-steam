# Name : Cynthia Wanjiru
# Date : 17/02/2026
# Program to display using shapes

n = 5
# Top part
for i in range(1, n +1):

    for a in range(n - 1):
        print("", end="")

    for star in range(2 * i - 1):
        print("*", end="")    


    print()

# bottom part
for i in range(n-1,0,-1):

    for s in range(n-i):
      print("", end="")  

    for star in range(2 * i - 1):
        print("*", end="")

    print()      