#Get user name,surname and bio
first_name = input("Enter your First name:").strip()
last_name = input("Enter your Last name:").strip()

bio = input("Enter your bio:").strip()
bio.replace("I am", "I'm")

#create a username 
username = f"{first_name[-1].lower()}{last_name.lower()}"
full_name = f"{first_name} {last_name}".title()

print(f"bio characters:{len(bio)}")
print(
    f"Your username is {username}"
    f"\nYour full name is {full_name}"
    f"\n{bio}"
)


