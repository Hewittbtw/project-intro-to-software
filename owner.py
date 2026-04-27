"""
owner.py

Contains the Owner class which represents a pet owner
and manages their list of pets.
"""

from pet import Pet
import utils


class Owner:
    """
    Represents a pet owner who can have multiple pets.
    """

    def __init__(self, name):
        """
        Initialise an Owner object.

        Args:
            name (str): Name of the owner
        """
        self.name = name
        self.pets = []

    def add_pet(self, name, species):
        """
        Create and add a new pet for this owner.

        Args:
            name (str): Name of the pet
            species (str): Species of the pet
        """
        new_pet = Pet(name, self, species)
        self.pets.append(new_pet)

    def find_pet(self, name):
        """
        Find a pet by name.

        Args:
            name (str): Name of the pet to search for

        Returns:
            Pet or None: Matching pet if found, otherwise None
        """
        return utils.find_by_name(name, self.pets)