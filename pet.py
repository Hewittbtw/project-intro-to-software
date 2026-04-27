"""
pet.py

Contains the Pet class which stores information about a pet,
including its owner, appointments, vaccinations, and prescriptions.
"""

from prescription import Prescription


class Pet:
    """
    Represents a pet belonging to an owner.
    Tracks appointments, vaccinations, and prescriptions.
    """

    def __init__(self, name, owner, species):
        """
        Initialise a Pet object.

        Args:
            name (str): Name of the pet
            owner (Owner): Owner of the pet
            species (str): Species of the pet
        """
        self.name = name
        self.owner = owner
        self.species = species

        self.appointments = []
        self.vaccinations = []
        self.prescriptions = []

    def create_prescription(self, medication, dosage):
        """
        Create a prescription for this pet.

        Args:
            medication (Medication): Medication prescribed
            dosage (int): Amount to be given

        Returns:
            Prescription: The created prescription object
        """
        prescription = Prescription(self, medication, dosage)
        self.prescriptions.append(prescription)
        return prescription

    def add_vaccination(self, vaccination):
        """
        Add a vaccination record to the pet.

        Args:
            vaccination: Vaccination object or record
        """
        self.vaccinations.append(vaccination)

    def add_appointment(self, appointment):
        """
        Add an appointment to the pet's record.

        Args:
            appointment (Appointment): Appointment object
        """
        self.appointments.append(appointment)