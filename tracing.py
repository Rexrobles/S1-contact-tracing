#Write a python program for contact tracing:

#- Display a menu of options
#	Menu:
#		 1 -> Add an item
#		 2 -> Search
#		 3 -> Exit (y/n)
#- Allow user to select item in the menu (check if valid)
#- Perform the selected option
#		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
#				   Use dictionary to store the info
#				   Use the full name as key
#				   The value is another dictionary of personal information
#		- Option 2: Search, ask full name then display the record
#		- Option 3: Ask the user if want to exit or retry.

#displaying option menu

print("""
  Menu:
    1 -> Add an item
    2 -> Search
    3 -> Exit (y/n)
""")

#asking user to select an item in the menu

userInput = int(input("What do you want to do? (1-3): "))

#if 1
if userInput == 1:
    # ask for the
    # # ask user  full name
    FullName = input("Enter your Full name: ")
    # ask user age
    age = input("Enter your age: ")
    # ask user address
    address = input("Enter your Address: ")
    # ask gender
    gender = input("Enter your Gender: ")
    # ask phone number
    phone = input("Enter your Phone Number: ")
    # ask email
    email = input("Enter your Email: ")
    # ask user bloodtype
    bloodtype = input("Enter your Bloodtype: ")
    # ask user hobby
    Hobby = input("Enter your Hobby: ")
    # ask user favorite food
    favorite = input("Enter your Favorite Food: ")
  
  