"""
veterinary_practice.py

Contains the VeterinaryPractice class which manages:
- owners and pets
- appointments
- medications
- prescriptions
"""


from medication import Medication
from owner import Owner
import utils


class veterinary_practice:
    """
    Core system class that manages all veterinary operations.
    """

    def __init__(self):
        self.owners = []
        self.medications = []
        self.prescriptions = []
        self.appointments = []

    # -------------------------
    # Registration / Pets

    def register_pet(self, pet_name, owner_name, species):
        owner = self.find_owner(owner_name)

        if owner is None:
            owner = Owner(owner_name)
            self.owners.append(owner)

        owner.add_pet(pet_name, species)

    # -------------------------
    # Appointments

    def create_appointment(self, appointment):
        self.appointments.append(appointment)
        return len(self.appointments) - 1

    def attend_appointment(self, appointment_id):
        appointment = self.find_appointment(appointment_id)

        if appointment is None:
            return "Unrecognized appointment ID"

        appointment.attend_appointment()
        return appointment.get_notes()

    # -------------------------
    # Medication (OBSERVER TRIGGER POINT)

    def stock_medication(self, medication_name, amount):
        medication = self.find_medication(medication_name)

        if medication is None:
            medication = Medication(medication_name, amount)
            self.medications.append(medication)
        else:
            medication.restock(amount)

        # Notify all prescriptions observing this medication
        medication.notify()

    # -------------------------
    # Prescription

    def create_prescription(self, pet, medication, dosage):
        prescription = pet.create_prescription(medication, dosage)
        self.prescriptions.append(prescription)
        return len(self.prescriptions) - 1

    def prepare_prescription_for_collection(self, prescription_id):
        prescription = self.find_prescription(prescription_id)

        if prescription is None:
            return "Unrecognized prescription ID"

        if prescription.prepare_for_collection():
            return "Prescription prepared"

        return "Prescription is not ready for preparation"

    def collect_prescription(self, prescription_id):
        prescription = self.find_prescription(prescription_id)

        if prescription is None:
            return "Unrecognized prescription ID"

        if prescription.collect():
            return "Prescription collected"

        return "Prescription is not ready for collection"

    # -------------------------
    # System checks

    def has_owners(self):
        return len(self.owners) > 0

    def has_medications(self):
        return len(self.medications) > 0

    def has_prescriptions(self):
        return len(self.prescriptions) > 0

    # -------------------------
    # Find methods

    def find_owner(self, name):
        return utils.find_by_name(name, self.owners)

    def find_medication(self, name):
        return utils.find_by_name(name, self.medications)

    def find_prescription(self, prescription_id):
        if 0 <= prescription_id < len(self.prescriptions):
            return self.prescriptions[prescription_id]
        return None

    def find_appointment(self, appointment_id):
        if 0 <= appointment_id < len(self.appointments):
            return self.appointments[appointment_id]
        return None