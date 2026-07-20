#Tracking individual letters
name = "Python"

#Use indexing to get the first and last letter of the string
print(name[-1]) #n
print(name[0]) #P
print(name[1]) #y
print(name[2]) #t
print(name[3]) #h
print(name[4]) #o
print(name[5]) #n

#Example of slicing
print(name[0:3]) #Pyt

#using string Methods
town = "  Pretoria "

#Uppercase, Lowercase and Strip methods
print(town.upper()) #PRETORIA
print(town.lower()) #pretoria   
print(town.strip()) #Pretoria

#Getting the length of a string
print(len('App Academy'))

#Creating a professional system email generator
first_name = input("Enter your First name:").strip()
last_name = input("Enter your Last name:").strip()

username = f"{first_name[0]}{last_name}"
print(f"Your email is: {username.lower()}@company.com")