# Name : Cynthia Wanjiru
# Date : 24/02/2026
# Program to perform file operations

# create new file
new_file = open("student_data.txt","r+") 


# write to new file
new_file.write("student name : Jenny Wambui, ID :34567891, email :cynthiawmmm@gmail.com")


# read from the new file
new_file = open("student_data.txt","r+") 
data = new_file.read()

print(data)

new_file.close()
#delete file
# use os module
import os 
os.remove("remove.txt")

#delete folder
os.rmdir("folder")