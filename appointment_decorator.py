"""
Decorator pattern for Appointment functionality.
Adds vaccinations and surgery notes when an appointment is attended.
"""

class AppointmentDecorator:
    def __init__(self, appointment):
        self.appointment = appointment

    def attend_appointment(self):
        return self.appointment.attend_appointment()

    def get_notes(self):
        return self.appointment.get_notes()


class VaccinationDecorator(AppointmentDecorator):
    def attend_appointment(self):
        super().attend_appointment()

        vaccination = input("Enter vaccination given: ")
        self.appointment.notes.append(f"vaccination={vaccination}")


class SurgeryDecorator(AppointmentDecorator):
    def attend_appointment(self):
        super().attend_appointment()

        surgery_notes = input("Enter surgery notes: ")
        self.appointment.notes.append(f"surgery notes={surgery_notes}")