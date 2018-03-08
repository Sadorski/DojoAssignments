class Patient(object):
    def __init__(self, uid, name, allergies, bednum="none"):
        self.uid = uid
        self.name = name
        self.allergies = allergies
        self.bednum = bednum

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity

    def admit(self, patient):
        if len(self.patients) < self.capacity:
            self.patients.append
            print "Patient has been successfully admitted"
        else:
            print "I'm sorry, this hospital is currently at Capacity."

    def discharge(self):
        pass

