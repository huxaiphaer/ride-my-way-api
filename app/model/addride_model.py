""" control properties of the order object"""
import uuid
import json


class AddRide():
    def __init__(self, id,  name, details, price):
        self.id = id
        self.name = name
        self.details = details
        self.price = price

    def json(self):
        """
        json representation of the Order model
        """
        return json.dumps({
            'id': self.id,
            'name': self.name,
            'details': self.details,
            'price':self.price
        })
