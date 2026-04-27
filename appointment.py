"""
appointment.py

Stores appointment details and allows notes to be recorded when an appointment is attended.
"""


class Appointment:
    """
    Represents a veterinary appointment for a pet.
    Stores appointment time and any notes recorded during attendance.
    """

    def __init__(self, pet, time):
        """
        Initialise an Appointment object.

        Args:
            pet (Pet): The pet the appointment is for
            time (str): Date and time of the appointment
        """
        self.pet = pet
        self.time = time

        # Register this appointment with the pet
        pet.add_appointment(self)

        # Notes collected when the appointment is attended
        self.notes = []

    def attend_appointment(self):
        """
        Record attendance details such as weight and health notes.
        """
        weight = input("Enter pet weight: ")
        self.notes.append(f"weight = {weight}")

        health_notes = input("Enter health notes: ")
        self.notes.append(health_notes)

    # --------------------
    # Getters

    def get_pet(self):
        """Return the pet associated with this appointment."""
        return self.pet

    def get_notes(self):
        """Return notes recorded during the appointment."""
        return self.notes