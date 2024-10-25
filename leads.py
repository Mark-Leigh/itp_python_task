class Lead:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        
class LeadList:
    def __init__(self):
        self.leads = []
        
    def add_lead(self, name, email, phone):
        new_lead = Lead(name, email, phone)
        self.leads.append(new_lead)
        
    def display_leads(self):
        for lead in self.leads:
            print(f'Name: {lead.name}, Email: {lead.email}, Phone: {lead.phone}')
            
    def delete_lead(self, name):
        for lead in self.leads:
            if lead.name == name:
                self.leads.remove(lead)
                break