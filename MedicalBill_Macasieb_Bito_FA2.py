class Patient:
    def __init__(self, name, bill_amount):
        self._name = name
        self._bill_amount = bill_amount
    def get_name(self):
        return self._name
    def get_bill_amount(self):
        return self._bill_amount
    def set_bill_amount(self,bill_amount):
        if bill_amount > 0:
            self._bill_amount = bill_amount
    def set_name(self,name):
        self._name = name
    def calculate_bill(self):
        return self._bill_amount
class SeniorPatient(Patient):
    def __init__(self, name,bill_amount):
        super().__init__(name, bill_amount)
    def calculate_bill(self):
        return self.get_bill_amount - (self.get_bill_amount * 0.15)
class PhilHealthPatient(Patient):
    def __init__(self, name,bill_amount):
        super().__init__(name, bill_amount)
    def calculate_bill(self):
        return self.get_bill_amount - (self.get_bill_amount * 0.20)

def print_patient(patients):
    print("Hospital Bill System")
    print("-"*20)
    for patient in patients:
        print("")
        print(f"Patient Name: {patient.get_name}")
        print(f"Original Bill: ₱ {patient.get_bill_amount:,.2f}")
        print(f"Final Bill: ₱ {patient.calculate_bill():,.2f}")

#main
regular_patient = Patient("Juan Dela Cruz",15000)
phil_health_patient = PhilHealthPatient("Maria Santos",15000)
senior_patient = SeniorPatient("Pedro Reyes",15000)
regular_patient.set_bill_amount = 175,000
patients = [regular_patient, phil_health_patient, senior_patient]
print_patient(patients)