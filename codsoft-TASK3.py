class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        if name in self.contacts:
            print(f"{name} is already in the contact book.")
        else:
            self.contacts[name] = phone
            print(f"Contact {name} added successfully.")

    def display_contacts(self):
        if self.contacts:
            print("\nContacts List:")
            for name, phone in self.contacts.items():
                print(f"Name: {name}, Phone number: {phone}")
        else:
            print("\nContact book is empty.")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Found Contact - Name: {name}, Phone: {self.contacts[name]}")
        else:
            print(f"{name} not found in the contact book.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name} has been deleted .")
        else:
            print(f"{name} not found.")

    def update_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
            print(f"{name}'s contact has been updated to {new_phone}.")
        else:
            print(f"{name} not found in the contact book.")

# Main program
def main():
    contact_book = ContactBook()

    while True:
        print("\n**Contact Book Menu**")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            contact_book.add_contact(name, phone)
        elif choice == '2':
            contact_book.display_contacts()
        elif choice == '3':
            name = input("Enter the name of the contact to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '5':
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter the new phone number: ")
            contact_book.update_contact(name, new_phone)
        elif choice == '6':
            print("Exiting Contact Book...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

