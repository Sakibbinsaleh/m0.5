from contact_manager import (
    add_contact,
    view_contacts,
    remove_contact,
    search_contacts,
    save_to_file,
    load_from_file,


)


def menu():

    filename = "contacts.txt"
    load_from_file(filename)



    while True:

        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contacts")
        print("5. Save and Exit")


        choice = input("Enter your choice (1-5): ")

        if choice == "1":

            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")

            if not phone.isdigit():


                print("Error: Phone number must be numeric!")
                continue

            add_contact(name, email, phone, address)
        elif choice == "2":


            view_contacts()
        elif choice == "3":
            phone = input("Enter the phone number of the contact to remove: ")
            remove_contact(phone)
        elif choice == "4":

            query = input("Enter name or phone to search: ")
            search_contacts(query)
        elif choice == "5":

            save_to_file(filename)

            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
