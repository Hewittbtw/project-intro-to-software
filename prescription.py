"""
prescription.py
"""

from enum import Enum


class PrescriptionStatus(Enum):
    PREPARING_ORDER = 1
    READY_FOR_COLLECTION = 2
    OUT_OF_STOCK = 3
    COLLECTED = 4


class Prescription:
    def __init__(self, pet, medication, dosage):
        self.pet = pet
        self.medication = medication
        self.dosage = dosage

        self.status = None
        self._set_initial_status()

        # Subscribe to medication updates
        self.medication.attach(self)

    def _set_initial_status(self):
        if self.medication.has_enough_stock(self.dosage):
            self.status = PrescriptionStatus.PREPARING_ORDER
        else:
            self.status = PrescriptionStatus.OUT_OF_STOCK

    # --------------------
    # Observer update method

    def update(self, medication):
        if self.status == PrescriptionStatus.READY_FOR_COLLECTION:
            self.medication.detach(self)
            return

        if medication.has_enough_stock(self.dosage):
            self.status = PrescriptionStatus.PREPARING_ORDER
        else:
            self.status = PrescriptionStatus.OUT_OF_STOCK

    # --------------------
    # Existing behaviour

    def prepare_for_collection(self):
        if self.status == PrescriptionStatus.PREPARING_ORDER:
            self.medication.reduce_stock(self.dosage)
            self.status = PrescriptionStatus.READY_FOR_COLLECTION
            self.medication.detach(self)
            return True
        return False

    def collect(self):
        if self.status == PrescriptionStatus.READY_FOR_COLLECTION:
            self.status = PrescriptionStatus.COLLECTED
            return True
        return False