def create_contact(name, phone):
    contacts = load_contacts_from_file()

    if name in contacts:
        return f"Name '{name}' already exists in the file."

    if any(contact['phone'] == phone for contact in contacts.values()):
        return f"Phone number '{phone}' already exists in the file."

    contacts[name] = {'phone': phone}
    save_contact(contacts)
    return f"Contact '{name}' created."


def view_contact(name):
    contacts = load_contacts_from_file()
    if name in contacts:
        contact = contacts[name]
        print(f"Name: '{name}', Phone: {contact['phone']}")
    else:
        print(f"Contact '{name}' not found.")


def edit_contact_menu():
    contacts = load_contacts_from_file()
    old_name = input("Enter the current contact name: ")

    if old_name not in contacts:
        print(f"Contact '{old_name}' not found.")
        return

    print("\nWhat do you want to edit?")
    print("1. Edit Name")
    print("2. Edit Phone Number")
    print("3. Edit Both Name and Phone Number")
    sub_choice = input("Enter your choice (1/2/3): ")

    if sub_choice == '1':
        new_name = input("Enter new name: ")

        if new_name in contacts:
            print(f"Contact name '{new_name}' already exists.")
            return

        contacts[new_name] = contacts.pop(old_name)
        save_contact(contacts)
        print(f"Name changed from '{old_name}' to '{new_name}'.")

    elif sub_choice == '2':
        new_phone = input("Enter new phone number: ")

        if any(contact['phone'] == new_phone and name != old_name for name, contact in contacts.items()):
            print(f"Phone number '{new_phone}' already exists.")
            return

        contacts[old_name]['phone'] = new_phone
        save_contact(contacts)
        print(f"Phone number for '{old_name}' updated to '{new_phone}'.")

    elif sub_choice == '3':
        new_name = input("Enter new name: ")
        new_phone = input("Enter new phone number: ")

        if new_name != old_name and new_name in contacts:
            print(f"Contact name '{new_name}' already exists.")
            return

        if any(contact['phone'] == new_phone and name != old_name for name, contact in contacts.items()):
            print(f"Phone number '{new_phone}' already exists.")
            return

        contacts[new_name] = contacts.pop(old_name)
        contacts[new_name]['phone'] = new_phone
        save_contact(contacts)
        print(f"Contact '{old_name}' updated to '{new_name}' with phone number '{new_phone}'.")

    else:
        print("Invalid choice. Returning to main menu.")


def delete_contact(name):
    contacts = load_contacts_from_file()
    if name in contacts:
        del contacts[name]
        save_contact(contacts)
        return f"Contact '{name}' deleted."
    else:
        return f"Contact '{name}' not found."


def save_contact(contacts):
    try:
        with open("file.txt", "w") as file:
            for name, contact in contacts.items():
                file.write(f"{name} - {contact['phone']}\n")
    except Exception as e:
        print(f"Error saving contacts: {e}")


def load_contacts_from_file():
    contacts = {}
    try:
        with open("file.txt", "r") as file:
            for line in file.readlines():
                name, phone = line.strip().split(" - ")
                contacts[name] = {'phone': phone}
    except FileNotFoundError:
        print("No existing contacts file found. Starting fresh.")
    return contacts


# Main loop
while True:
    print("\nContact options")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Edit Contact (Name and/or Phone)")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        print(create_contact(name, phone))

    elif choice == '2':
        name = input("Enter name to view: ")
        view_contact(name)

    elif choice == '3':
        edit_contact_menu()

    elif choice == '4':
        name = input("Enter name to delete: ")
        print(delete_contact(name))

    elif choice == '5':
        contacts = load_contacts_from_file()
        if contacts:
            print("All contacts:")
            for name, contact in contacts.items():
                print(f"Name: {name}, Phone: {contact['phone']}")
        else:
            print("No contacts found.")

    elif choice == '6':
        break

    else:
        print("Invalid choice. Please try again.")
