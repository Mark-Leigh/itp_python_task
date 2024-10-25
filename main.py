import json
from contacts import ContactList
from leads import LeadList
from registrations import RegistrantList
from checks_and_updates import CheckRegistrantMatch

# JSON data
contacts_json_data = '''
[
    {"name": "Alice Brown", "email": null, "phone": "1231112223"},
    {"name": "Bob Crown", "email": "bob@crowns.com", "phone": null},
    {"name": "Carlos Drew", "email": "carl@drewess.com", "phone": "3453334445"},
    {"name": "Doug Emerty", "email": null, "phone": "4564445556"},
    {"name": "Egan Fair", "email": "eg@fairness.com", "phone": "5675556667"}
]
'''

leads_json_data = '''
[
    {"name": null, "email": "kevin@keith.com", "phone": null},
    {"name": "Lucy", "email": "lucy@liu.com", "phone": "3210001112"},
    {"name": "Mary Middle", "email": "mary@middle.com", "phone": "3331112223"},
    {"name": null, "email": null, "phone": "4442223334"},
    {"name": null, "email": "ole@olson.com", "phone": null}
]
'''

registrants_json_data = '''
[
    {"name": "Lucy Liu", "email": "lucy@liu.com", "phone": null},
    {"name": "Doug", "email": "doug@emmy.com", "phone": "4564445556"},
    {"name": "Uma Thurman", "email": "uma@thurs.com", "phone": null}
]
'''

# Load JSON data
contacts_data = json.loads(contacts_json_data)
leads_data = json.loads(leads_json_data)
registrants_data = json.loads(registrants_json_data)

# Create ContactList instance
contact_list = ContactList()

# Create LeadList instance
lead_list = LeadList()

# Create RegistrantList instance
registrant_list = RegistrantList()

# Add contacts from JSON data
for contact in contacts_data:
    contact_list.add_contact(contact["name"], contact["email"], contact["phone"])
    
# Add leads from JSON data
for lead in leads_data:
    lead_list.add_lead(lead["name"], lead["email"], lead["phone"])
    
# Add registrants from JSON data
for registrant in registrants_data:
    registrant_list.add_registrant(registrant["name"], registrant["email"], registrant["phone"])

system = CheckRegistrantMatch(contact_list.contacts, lead_list.leads)
    
# Display contacts, Leads, and Registrants
print('Initial Contacts:')
contact_list.display_contacts()

print('\nInitial Leads:')
lead_list.display_leads()

print('\nInitial Registrants:')
registrant_list.display_registrants()

for registrant in registrant_list:
    system.register(registrant)

# Display final contacts and leads
print('\nFinal Contacts:')
contact_list.display_contacts()

print('\nFinal Leads:')
lead_list.display_leads()
