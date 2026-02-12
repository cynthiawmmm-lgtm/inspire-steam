# Name : Cynthia Wanjiru
# Date : 12/02/2026
# string formatting

#get string length
sentence = "I watch movies"

string_length = len(sentence)

print(f"the length is: {string_length}")

#spliting a string
sentence_2 = "mathematics physics"
split = sentence_2.split (" ")

print(f"the first subject is:",split[0] )

#make everything CAPS
mpesa_code = "ub21ddsfgh"

capitalized = mpesa_code.upper()

print("new mpesa code:",capitalized)
#make everything lower case
mpesa_code = "ub21ddsfhg"


decapitalize= mpesa_code.lower()

print("new mpesa code:",decapitalize)
#replacing characters in a string

balance = "200kes"
amount_added = "300kes"

cleaned_balance = balance.replace ("kes", "")

print("cleaned balance:", cleaned_balance)

cleaned_amount_added = amount_added.replace ("kes", "")

print("cleaned amount added:", cleaned_amount_added)

new_balance = int(cleaned_balance) + int(cleaned_amount_added)

print(f"the new balance is:",new_balance)