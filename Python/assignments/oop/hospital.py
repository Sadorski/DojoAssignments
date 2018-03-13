class Patient(object):
    class_counter=1
    def __init__(self, name, allergies, bednum="none"):
        self.name = name
        self.allergies = allergies
        self.bednum = bednum
        self.uid = Patient.class_counter
        Patient.class_counter += 1

    def __str__(self):
        return "{} {} {} {}".format(self.uid, self.name, self.allergies, self.bednum)

class Hospital(object):
    
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
        self.
        )

    def admit(self, patient):
        if len(self.patients) < self.capacity:
            patient.bednum = self.beds.pop()
            self.patients.append(patient)
            print "Patient has been successfully admitted"
        else:
            print "I'm sorry, this hospital is currently at Capacity."
        return self

    def discharge(self, name):
        for patient in self.patients:
            if patient.name == name:
                self.beds.append(patient.bednum)
                self.patients.remove(patient)

        return self
        
       

    def show(self):
        for i in self.patients:
            print i



sacred_heart = Hospital("Sacred Heart", 100)
sacred_heart.admit(Patient("Betty", "None"))
sacred_heart.admit(Patient("Zach", "Peanuts"))
sacred_heart.admit(Patient("Victor", "none"))
sacred_heart.discharge("Zach")
sacred_heart.show()




        

