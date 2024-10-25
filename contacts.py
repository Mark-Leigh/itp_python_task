class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, email, phone):
        new_contact = Contact(name, email, phone)
        self.contacts.append(new_contact)

    def display_contacts(self):
        for contact in self.contacts:
            print(f'Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}')


