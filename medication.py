"""
medication.py
"""

from abc import ABC, abstractmethod


class Medication:
    def __init__(self, name, amount_in_stock):
        self.name = name
        self.amount_in_stock = amount_in_stock
        self._observers = []

    # --------------------
    # Observer pattern

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    # --------------------
    # Stock logic

    def restock(self, amount):
        self.amount_in_stock += amount
        self.notify()

    def reduce_stock(self, amount):
        self.amount_in_stock -= amount

    def has_enough_stock(self, dosage):
        return self.amount_in_stock >= dosage