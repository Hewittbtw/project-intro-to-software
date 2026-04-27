"""
medication.py

Contains the Medication class which tracks stock levels and allows
stock management operations such as restocking and reducing stock.
"""


class Medication:
    """
    Represents a medication with a name and stock level.
    """

    def __init__(self, name, amount_in_stock):
        """
        Initialise a Medication object.

        Args:
            name (str): Name of the medication
            amount_in_stock (int): Initial stock level
        """
        self.name = name
        self.amount_in_stock = amount_in_stock

    def restock(self, amount):
        """
        Increase stock by a given amount.

        Args:
            amount (int): Amount to add to stock
        """
        self.amount_in_stock += amount

    def reduce_stock(self, amount):
        """
        Decrease stock by a given amount.

        Args:
            amount (int): Amount to remove from stock
        """
        self.amount_in_stock -= amount

    def has_enough_stock(self, dosage):
        """
        Check if there is enough stock for a given dosage.

        Args:
            dosage (int): Required amount

        Returns:
            bool: True if enough stock exists, otherwise False
        """
        return self.amount_in_stock >= dosage