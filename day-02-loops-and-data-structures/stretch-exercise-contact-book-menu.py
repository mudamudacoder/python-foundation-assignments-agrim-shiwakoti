'''
Stretch Exercise: Contact Book Menu
Student: Agrim Shiwakoti
Day: 2
'''

#input values


contacts = {}

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Adding contact
    if choice == '1':
        name = input("Enter contact name: ").title() #title case to ensure consistent formatting of names
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact '{name}' with phone number '{phone}' and email '{email}' added.")

    # Searching contact
    elif choice == '2':
        search_name = input("Enter the name of the contact to search: ").title()
        if search_name in contacts:
            print(f"Contact found: Name: {search_name}, Phone: {contacts[search_name]['phone']}, Email: {contacts[search_name]['email']}")
        else:
            print(f"Contact '{search_name}' not found.")  #error handling for contact not found

    # Deleting contact
    elif choice == '3':
        delete_name = input("Enter the name of the contact to delete: ").title()
        if delete_name in contacts:
            del contacts[delete_name] #using inbuilt method del to delete the contact from the dictionary
            print(f"Contact '{delete_name}' deleted.")
        else:
            print(f"Contact '{delete_name}' not found.")  #error handling for contact not found

    # Displaying all contacts
    elif choice == '4':
        
        if contacts:
            print("All Contacts:")
            for name, info in contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
        else:
            print("\nNo contacts found.")

    # Exiting the program
    elif choice == '5':
       
        print("Exiting the Contact Book Menu.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")