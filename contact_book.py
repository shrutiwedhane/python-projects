contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact added successfully!")

def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print("Name:", name)
        print("Phone:", contacts[name])
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def view_contacts():
    if not contacts:
        print("No contacts available!")
    else:
        for name, phone in contacts.items():
            print(name, ":", phone)

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        view_contacts()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
