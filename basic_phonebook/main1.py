class ph_book():
    def __init__(self):
        self.contacts = self.load_contacts_from_file()

    def create_contact(self, name, phone):
        if name in self.contacts:
            return f"Name '{name}' already exists in the file."

        if any(contact['phone'] == phone for contact in self.contacts.values()):
            return f"Phone number '{phone}' already exists in the file."

        self.contacts[name] = {'phone': phone}
        self.save_contact()
        return f"Contact '{name}' created."

    def view_contact(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            print(f"Name: '{name}', Phone: {contact['phone']}")
        else:
            print(f"Contact '{name}' not found.")

    def edit_contact_menu(self):
        old_name = input("Enter the current contact name: ")

        if old_name not in self.contacts:
            print(f"Contact '{old_name}' not found.")
            return

        print("\nWhat do you want to edit?")
        print("1. Edit Name")
        print("2. Edit Phone Number")
        print("3. Edit Both Name and Phone Number")
        sub_choice = input("Enter your choice (1/2/3): ")

        if sub_choice == '1':
            new_name = input("Enter new name: ")

            if new_name in self.contacts:
                print(f"Contact name '{new_name}' already exists.")
                return

            self.contacts[new_name] = self.contacts.pop(old_name)
            self.save_contact()
            print(f"Name changed from '{old_name}' to '{new_name}'.")

        elif sub_choice == '2':
            new_phone = input("Enter new phone number: ")

            if any(contact['phone'] == new_phone and name != old_name for name, contact in self.contacts.items()):
                print(f"Phone number '{new_phone}' already exists.")
                return

            self.contacts[old_name]['phone'] = new_phone
            self.save_contact()
            print(f"Phone number for '{old_name}' updated to '{new_phone}'.")

        elif sub_choice == '3':
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")

            if new_name != old_name and new_name in self.contacts:
                print(f"Contact name '{new_name}' already exists.")
                return

            if any(contact['phone'] == new_phone and name != old_name for name, contact in self.contacts.items()):
                print(f"Phone number '{new_phone}' already exists.")
                return

            self.contacts[new_name] = self.contacts.pop(old_name)
            self.contacts[new_name]['phone'] = new_phone
            self.save_contact()
            print(f"Contact '{old_name}' updated to '{new_name}' with phone number '{new_phone}'.")

        else:
            print("Invalid choice. Returning to main menu.")


    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contact()
            return f"Contact '{name}' deleted."
        else:
            return f"Contact '{name}' not found."


    def save_contact(self):
        try:
            with open("file.txt", "w") as file:
                for name, contact in self.contacts.items():
                    file.write(f"{name} - {contact['phone']}\n")
        except Exception as e:
            print(f"Error saving contacts: {e}")


    def load_contacts_from_file(self):
        contacts = {}
        try:
            with open("file.txt", "r") as file:
                for line in file.readlines():
                    name, phone = line.strip().split(" - ")
                    contacts[name] = {'phone': phone}
        except FileNotFoundError:
            print("No existing contacts file found. Starting fresh.")
        return contacts

# Create an instance of the ph_book class
phone_book = ph_book()

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
        print(phone_book.create_contact(name, phone))

    elif choice == '2':
        name = input("Enter name to view: ")
        phone_book.view_contact(name)

    elif choice == '3':
        phone_book.edit_contact_menu()

    elif choice == '4':
        name = input("Enter name to delete: ")
        print(phone_book.delete_contact(name))

    elif choice == '5':
        if phone_book.contacts:
            print("All contacts:")
            for name, contact in phone_book.contacts.items():
                print(f"Name: {name}, Phone: {contact['phone']}")
        else:
            print("No contacts found.")

    elif choice == '6':
        break

    else:
        print("Invalid choice. Please try again.")