""" control properties of the order object"""
import uuid
import json


class AddRide():
    def __init__(self, id,  offer_name, offer_details, offer_price):
        self.id = id
        self.offer_name = offer_name
        self.offer_details = offer_details
        self.offer_price = offer_price

    def json(self):
        """
        json representation of the Order model
        """
        return json.dumps({
            'id': self.id,
            'offer_name': self.offer_name,
            'offer_details': self.offer_details,
            'offer_price':self.offer_price
        })
