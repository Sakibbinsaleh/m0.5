contacts = []

def add_contact(name, email, phone, address):

    for contact in contacts:


        if contact["phone"] == phone:
            print("Phone number already exists!")
            return False
        

    contact = {"name": name, "email": email, "phone": phone, "address": address}
    contacts.append(contact)

    print("Contact added successfully!")
    return True

def view_contacts():

    if not contacts:
        print("No contacts available!")
        return
    

    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):

        print(f"{i}. Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")

    print()

def remove_contact(phone):

    for contact in contacts:


        if contact["phone"] == phone:

            contacts.remove(contact)
            print("Contact removed successfully!")

            return True
    print("Error: Contact not found!")

    return False


def search_contacts(query):
    results = [contact for contact in contacts if query.lower() in contact["name"].lower() or query in contact["phone"]]
    if not results:


        print("No matching contacts found!")
        return
    print("\nSearch Results:")

    for contact in results:
        print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")

    print()


def save_to_file(filename):
    try:

        with open(filename, "w") as file:
            for contact in contacts:
                file.write(f"{contact['name']},{contact['email']},{contact['phone']},{contact['address']}\n")

        print("Contacts saved to file successfully!")
    except Exception as e:
        print(f"Error saving to file: {e}")


def load_from_file(filename):
    try:
        with open(filename, "r") as file:
            for line in file:

                name, email, phone, address = line.strip().split(",")
                contacts.append({"name": name, "email": email, "phone": phone, "address": address})
        print("Contacts loaded from file successfully!")

        
    except FileNotFoundError:
        print("No file found. Starting with an empty contact list.")
    except Exception as e:
        print(f"Error loading file: {e}")
