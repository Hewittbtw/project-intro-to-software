"""
prescription.py

Contains the Prescription class and PrescriptionStatus enum.
Tracks the lifecycle of a prescription from creation to collection.
"""

from enum import Enum


class PrescriptionStatus(Enum):
    """
    Represents the possible states of a prescription.
    """
    PREPARING_ORDER = 1
    READY_FOR_COLLECTION = 2
    OUT_OF_STOCK = 3
    COLLECTED = 4


class Prescription:
    """
    Represents a prescription for a pet and medication.

    Lifecycle:
    - PREPARING_ORDER: medication is in stock and ready to be prepared
    - OUT_OF_STOCK: insufficient stock available
    - READY_FOR_COLLECTION: medication prepared
    - COLLECTED: medication has been collected
    """

    def __init__(self, pet, medication, dosage):
        """
        Initialise a Prescription object.

        Args:
            pet (Pet): The pet the prescription is for
            medication (Medication): The medication prescribed
            dosage (int): Amount of medication required
        """
        self.pet = pet
        self.medication = medication
        self.dosage = dosage

        self._set_initial_status()

    def _set_initial_status(self):
        """
        Set initial prescription status based on stock availability.
        """
        if self.medication.has_enough_stock(self.dosage):
            self.status = PrescriptionStatus.PREPARING_ORDER
        else:
            self.status = PrescriptionStatus.OUT_OF_STOCK

    def prepare_for_collection(self):
        """
        Prepare prescription for collection if possible.

        Returns:
            bool: True if successfully prepared, otherwise False
        """
        if self.status == PrescriptionStatus.PREPARING_ORDER:
            self.medication.reduce_stock(self.dosage)
            self.status = PrescriptionStatus.READY_FOR_COLLECTION
            return True
        return False

    def collect(self):
        """
        Mark prescription as collected if ready.

        Returns:
            bool: True if successfully collected, otherwise False
        """
        if self.status == PrescriptionStatus.READY_FOR_COLLECTION:
            self.status = PrescriptionStatus.COLLECTED
            return True
        return False