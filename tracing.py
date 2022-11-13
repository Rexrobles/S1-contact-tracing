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

#displaying empty main dictionary
Data = {}
#displaying option menu

print("""
  Menu:
    \033[34;4m1 -> Add an item\033[0m 
    \033[34;4m2 -> Search\033[0m
    \033[34;4m3 -> Exit (y/n)\033[0m
""")

#asking user to select an item in the menu
while True:
  userInput = int(input("\n\033[35;2mWhat do you want to do? (1-3)\033[0m: "))

  #if 1
  if userInput == 1:
        
      # ask for the
      # # ask user  full name
      print(">> Please Add your Information <<")
      FullName = input("Enter your Full name: ")
      # ask user 
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
    
    # add in dictionary variable
      Data[FullName] = {
          "Name": FullName,
          "Age": age,
          "Address": address,
          "Gender": gender,
          "Phone": phone,
          "Email": email,
          "Bloodtype": bloodtype,
          "Hobby": Hobby,
          "FavoriteFood": favorite,
      }
    # print saved if added
      print("\n\033[31;1mInformation saved!\033[0m")
      print()
      
  # if 2
  elif userInput == 2:
  # Searching if the name is in the dictionary list
      print("")
      print("\033[32;1m=====Searching Item=====\033[0m")
      print()
      search = input("\037[31;3mEnter the Name you want to Search\033[0m: ")
      if search in Data:
            print("Name: " + Data[search]["Name"])
            print("Age: " + Data[search]["Age"])
            print("Address: " + Data[search]["Address"])
            print("Gender: " + Data[search]["Gender"])
            print("Phone: " + Data[search]["Phone"])
            print("Email: " + Data[search]["Email"])
            print("Bloodtype: " + Data[search]["Bloodtype"])
            print("Hobby: " + Data[search]["Hobby"])
            print("FavoriteFood: " + Data[search]["FavoriteFood"])
           
    # if no, print no records found
      else:
        print("\033[32;1mNo record saved!\033[0m")
    # if 3
  # ask the user if they want to exit y/n
  elif userInput == 3:
        y_or_no = input("Do you want to exit?\n Type yes/no: ")   
        if y_or_no == "yes":
            break
        elif y_or_no == "no":
              continue
print("THANK YOU!!")