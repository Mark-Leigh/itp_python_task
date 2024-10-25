# Class to check registant to contacts and leads

class Registrant:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        
class RegistrantList:
    def __init__(self):
        self.registrants = []

    def add_registrant(self, name, email, phone):
        self.registrants.append({"name": name, "email": email, "phone": phone})

    def display_registrants(self):
        for registrant in self.registrants:
            print(f'Name: {registrant["name"]}, Email: {registrant["email"]}, Phone: {registrant["phone"]}')

    def __iter__(self):
        return iter(self.registrants)
