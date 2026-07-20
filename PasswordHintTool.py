import maskpass
#Get user's password: user input is masked for security 
password = maskpass.askpass("Enter a secure password: ").strip()

#Loop that will keep asking for a new password until it is valid
while len(password) < 8 or len(password) > 12:
    if len(password) < 8:
        print("Password is too short, please enter a password with more than 8 characters.")
    elif len(password) > 12:
        print("Password is too long, please enter a password with less than 12 characters.")
    
    #Ask for the password again inside the loop to avoid an infinite loop
    password = maskpass.askpass("Enter a secure password: ").strip()

print("Password is valid 👌")

# Create the password hint: Uses indexing to get the first and last character of the password
a = password[0]
b = password[-1]
print("Your password hint is: Your password starts with " + a + " and ends with " + b)
