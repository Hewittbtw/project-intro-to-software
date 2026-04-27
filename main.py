"""
main.py

Starts the Veterinary Practice application and contains the UserInterface class.
The UI menu is displayed until the user chooses to exit.
"""

from appointment import Appointment
from veterinary_practice import veterinary_practice


class UserInterface:
    """
    Handles user interaction and menu navigation for the veterinary system.
    """

    def __init__(self, vp):
        """
        Initialise the user interface.

        Args:
            vp (veterinary_practice): The veterinary practice system instance.
        """
        self.vp = vp

    def menu(self):
        """
        Display menu options and process user selection.

        Returns:
            bool: False if user chooses to exit, otherwise True.
        """

        print("\nSelect one of the following options:")
        print("  1. Register a pet")
        print("  2. Book an appointment")
        print("  3. Attend an appointment")
        print("  4. Stock/re-stock a medication")
        print("  5. Create a prescription")
        print("  6. Prepare a prescription for collection")
        print("  7. Pick-up a prescription")
        print("  8. Exit")

        try:
            option = int(input("Enter option number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return True

        match option:
            case 1:
                self.register_pet()
            case 2:
                self.book_appointment()
            case 3:
                self.attend_appointment()
            case 4:
                self.stock_medication()
            case 5:
                self.create_prescription()
            case 6:
                self.prepare_prescription()
            case 7:
                self.collect_prescription()
            case 8:
                return False
            case _:
                print("Unknown option selected")

        return True

    def register_pet(self):
        """Register a new pet with its owner."""
        owner_name = input("Enter owner's name: ")
        pet_name = input("Enter pet's name: ")
        species = input("Enter pet's species: ")

        self.vp.register_pet(pet_name, owner_name, species)

    def book_appointment(self):
        """Book an appointment for an existing pet."""
        if not self.vp.has_owners():
            print("Register a pet first!")
            return

        pet = self._enter_details_to_find_existing_pet()

        time = input("Enter appointment date and time (any string): ")

        appointment = Appointment(pet, time)

        appointment_id = self.vp.create_appointment(appointment)
        print(f"The appointment ID is {appointment_id}")

    def attend_appointment(self):
        """Mark an appointment as attended and display notes."""
        appointment_id = int(input("Enter appointment ID: "))
        notes = self.vp.attend_appointment(appointment_id)
        print(f"Appointment notes: {notes}")

    def stock_medication(self):
        """Add stock for a medication."""
        medication_name = input("Enter medication name: ")
        amount = int(input("Enter amount delivered: "))

        self.vp.stock_medication(medication_name, amount)

    def create_prescription(self):
        """Create a prescription for a pet."""
        if not self.vp.has_owners() or not self.vp.has_medications():
            print("Register a pet and stock medications first!")
            return

        pet = self._enter_details_to_find_existing_pet()

        medication = None
        while not medication:
            medication_name = input("Enter medication name: ")
            medication = self.vp.find_medication(medication_name)

        dosage = int(input("Enter dosage (amount to be given): "))

        prescription_id = self.vp.create_prescription(pet, medication, dosage)
        print(f"The prescription ID is {prescription_id}")

    def prepare_prescription(self):
        """Prepare a prescription for collection."""
        prescription_id = int(input("Enter prescription ID: "))
        result = self.vp.prepare_prescription_for_collection(prescription_id)
        print(result)

    def collect_prescription(self):
        """Mark a prescription as collected."""
        prescription_id = int(input("Enter prescription ID: "))
        result = self.vp.collect_prescription(prescription_id)
        print(result)

    # --------------------
    # Helper methods

    def _enter_existing_owner(self):
        """Prompt until a valid owner is found."""
        owner = None
        while not owner:
            owner_name = input("Enter owner's name: ")
            owner = self.vp.find_owner(owner_name)
        return owner

    def _enter_details_to_find_existing_pet(self):
        """Prompt until a valid pet is found for an existing owner."""
        owner = self._enter_existing_owner()

        pet = None
        while not pet:
            pet_name = input("Enter pet's name: ")
            pet = owner.find_pet(pet_name)

        return pet


# ------------------------------

if __name__ == "__main__":
    ui = UserInterface(veterinary_practice())

    running = True
    while running:
        running = ui.menu()