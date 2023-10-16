phonebook = {
  "Naomi Chege": "0722456393",
  "Fauzia Njoki": "0706561871",
  "Pauline Mugwe": "0713338414",
  "Sharon Mumbi": "0702899842"
}

def add_contact():
  name = input("Enter contact name: ")
  if name in phonebook:
    print("Contact already exists.")
  else:
    phone = input("Enter contact phone number: ")
    phonebook[name] = phone
    print("Contact added successfully.")

def delete_contact():
  name = input("Enter the contact name you'd like to delete: ")
  if name in phonebook:
    del phonebook[name]
    print("Contact deleted successfully.")
  else:
    print("Contact not found.Cannot be deleted")


def search_contact():
  name = input("Enter contact name you want to search: ")
  if name in phonebook:
    print("Contact found. Phone number is: ", phonebook[name])
  else:
    print("Contact not found.")

def print_contacts():
  if phonebook:
    print("Contacts in the phonebook: ")
    for name, phone in phonebook.items():
      print(name, phone)
  else:
    print("Phonebook is empty.")

while True:
 print("\nWelcome to the phonebook menu: ")
 print("1. Add contact")
 print("2. Delete contact")
 print("3. Search contact")
 print("4. Print all contacts")
 print("5. Exit")

 choice = input("Enter your choice 1/2/3/4/5: ")

 if choice == "1":
  add_contact()  
 elif choice == "2":
  delete_contact()  
 elif choice == "3":
  search_contact()  
 elif choice == "4":
  print_contacts()  
 elif choice == "5":
  print("Exiting the phonebook.")
  break
else:
  print("Invalid option. Please choose either 1,2,3,4 or 5.")