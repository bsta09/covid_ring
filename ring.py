import random
from datetime import date


# today = date.today()
# another_day = date(2020, 3, 20)

# delta = today - another_day

# print(delta)

id_num = random.randint(1,10)

class Ring:
    def __init__(self, id_num):
        self.id = id_num
        self.contacts = {}
        self.status = False
        self.light = 'blue'

    def contact_check(self):
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
        self.contacts[ring2]['contact_count'] += 1
        self.contacts[ring2]['contact_date'].append(self.date)
        self.contacts[ring2]['status'] = ring2.status
        
    def contact(self, ring2, date):
        self.date = date
        if ring2 in self.contacts.keys():
            self.increment_contact(ring2)
        else:
            self.first_contact(ring2)

    def status_change(self):
        if self.status == False:
            self.status = True
            self.light = 'flashing red'
            self.contact_check()
        else:
            self.status = False
            self.light = 'blue'
            self.contact_check()



