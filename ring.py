import random
from datetime import date


id_num = random.randint(1,10)

class Ring:
    def __init__(self, id_num):
        self.id = id_num
        self.contacts = {}
        self.status = False
        self.light = 'blue'

    def contact_check(self):
        """ Check all contacts in dict, and cross-check for contacts 
            within past 14 days

            Change ring2's light to flashing red for >1 contacs, warning
            warning yellow for 1 contact """
        for key in self.contacts.keys():
            most_recent_contact = self.contacts[key]['contact_date'][-1]
            delta = date.today() - most_recent_contact
            if delta.days <= 14 and self.contacts[key]['contact_count'] >1:
                key.light = 'flashing red'
            elif delta.days <= 14 and self.contacts[key]['contact_count'] == 1:
                key.light = 'yellow'

    def first_contact(self, ring2):
        """ Log contact with another ring and increment amount as dict value """
        self.contacts[ring2] = {}
        self.contacts[ring2]['contact_count'] = 1
        self.contacts[ring2]['contact_date'] = []
        self.contacts[ring2]['contact_date'].append(self.date)
        self.contacts[ring2]['status'] = ring2.status

    def increment_contact(self, ring2):
        """ Log contact with another ring and increment amount as dict value """
        self.contacts[ring2]['contact_count'] += 1
        self.contacts[ring2]['contact_date'].append(self.date)
        self.contacts[ring2]['status'] = ring2.status
        
    def contact(self, ring2, date):
        """ To be used when 2 rings come within arbitrary contact"""
        self.date = date
        if ring2 in self.contacts.keys():
            self.increment_contact(ring2)
        else:
            self.first_contact(ring2)

    def status_change(self):
        """ To be used when wearer receives positive result sends warnings to close
            contacts via change in receiver's light"""
        if self.status == False:
            self.status = True
            self.light = 'flashing red'
            self.contact_check()
        else:
            self.status = False
            self.light = 'blue'
            self.contact_check()



