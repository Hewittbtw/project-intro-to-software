"""
test_application.py

Basic tests for the veterinary practice application.
"""

from appointment import Appointment
from prescription import PrescriptionStatus
from veterinary_practice import veterinary_practice
import appointment


def setup_system():
    """
    Create a fresh veterinary practice instance with one test pet.

    Returns:
        tuple: (vp, pet)
    """
    vp = veterinary_practice()
    vp.register_pet("Kitty", "Tim", "cat")
    pet = vp.find_owner("Tim").find_pet("Kitty")
    return vp, pet


def test_register_pet():
    vp, _ = setup_system()

    owner = vp.find_owner("Tim")
    assert owner.name == "Tim"

    pet = owner.find_pet("Kitty")
    assert pet.name == "Kitty"


def test_appointments():
    vp, pet = setup_system()

    # Mock input
    appointment.input = lambda prompt=None: "input"

    a = Appointment(pet, "Today")
    vp.create_appointment(a)

    notes = vp.attend_appointment(0)

    assert notes == ["weight= input", "input"]


def test_prescription_too_little_stock():
    vp, pet = setup_system()

    vp.stock_medication("med1", 3)
    med = vp.find_medication("med1")

    id = vp.create_prescription(pet, med, 5)
    prescription = vp.find_prescription(id)

    assert prescription.status == PrescriptionStatus.OUT_OF_STOCK


def test_prescription_with_stock():
    vp, pet = setup_system()

    vp.stock_medication("med1", 3)
    med = vp.find_medication("med1")

    id = vp.create_prescription(pet, med, 2)
    prescription = vp.find_prescription(id)

    assert prescription.status == PrescriptionStatus.PREPARING_ORDER

    vp.prepare_prescription_for_collection(id)
    assert prescription.status == PrescriptionStatus.READY_FOR_COLLECTION

    vp.collect_prescription(id)
    assert prescription.status == PrescriptionStatus.COLLECTED