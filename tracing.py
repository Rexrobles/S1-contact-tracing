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
    # ask for the
    # # ask user  full name
    # ask user age
    # ask user address
    # ask gender
    # ask phone number
    # ask email
    # ask user work
    
  # add in dictionary variable
  # print saved if added
  
# if 2
# Searching if the name is in the dictionary list
  # if yes, display all the information
  # if no, print no records found
  
  # if 3
# ask the user if they want to exit y/n
# if exit, exit the program
