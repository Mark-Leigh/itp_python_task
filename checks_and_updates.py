from contacts import Contact
from leads import Lead

class CheckRegistrantMatch:
    def __init__(self, contacts, leads): 
        self.contacts = contacts
        self.leads = leads

 
    def register(self, registrant):
        name = registrant["name"]
        email = registrant["email"]
        phone = registrant["phone"]

        def match_and_update(targets):
            for target in targets:
                if (target.email == email and email) or (target.phone == phone and phone):
                    if not target.name: target.name = name
                    if not target.email and email: target.email = email
                    if not target.phone and phone: target.phone = phone
                    return True
            return False

        # Step 1: Try to match registrant's email to contacts
        if match_and_update(self.contacts):
            return

        # Step 2: Try to match registrant's phone to contacts
        if match_and_update(self.contacts):
            return

        # Step 3: Match registrant's email to leads
        for lead in self.leads:
            if lead.email == email:
                self.contacts.append(Contact(name, email, lead.phone or phone))
                self.leads.remove(lead)
                return

        # Step 4: Match registrant's phone to leads
        for lead in self.leads:
            if lead.phone == phone:
                self.contacts.append(Contact(name, lead.email or email, phone))
                self.leads.remove(lead)
                return

        # Step 5: Add as new contact if no matches found
        self.contacts.append(Contact(name, email, phone))
                
    def update_contact(self, contact, name, other):
        if not contact.name:
            contact.name = name
        if not contact.email and "@" in other:
            contact.email = other
        if not contact.phone and other.isdigit():
            contact.phone = other
            