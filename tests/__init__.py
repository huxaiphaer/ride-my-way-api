import os
import sys
sys.path.append(os.getcwd())
import unittest
import json
from app import app, config
from app.config import app_config
from app.rides.managerides import rides_list
from app.user.authentication import my_users_list

class BaseTestCase(unittest.TestCase):
    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        app.config.from_object(app_config["testing"])
        return app

    def setUp(self):
        self.client = app.test_client(self)

    def tearDown(self):
        """
        Drop the data structure data
        """
        rides_list[:] = []
        my_users_list[:] = []

    def register_user(self, username, email, password, isDriver):
        """
        Method for registering a user with dummy data
        """
        return self.client.post(
            'api/v1/signup',
            data=json.dumps(dict(
                username=username,
                email=email,
                password=password,
                isDriver=isDriver
            )
            ),
            content_type='application/json'
        )

    def login_user(self, email, password):
        """
        Method for logging a user with dummy data
        """
        return self.client.post(
            'api/v1/login',
            data=json.dumps(
                dict(
                    email=email,
                    password=password
                )
            ),
            content_type='application/json'
        )

    def get_token(self):
        """
        Returns a user token
        """
        response = self.login_user("huz@gmail.com", "12345")
        data = json.loads(response.data.decode())
        return data['token']

    def add_ride(self, name, details, price,token):
        """
        Function to create a request
        """
        return self.client.post(
            '/api/v1/rides',
            data=json.dumps(
                dict(
                    name=name,
                    details=details,
                    price=price
                )
            ),
            content_type='application/json',
            headers=({"token": token})
        )
    def get_rideoffers(self, token):
        """
        function to return get
        """
        return self.client.get('/api/v1/rides', headers=({"token": token}))

    def get_one_rideoffer(self, token):
        """
        function to return get
        """
        return self.client.get('/api/v1/rides/<ride_id>{}'.format(id), headers=({"token": token}))

    def request_ride_offer(self,rideId,token):
        
         return self.client.post(
           '/api/v1/<rideId>/requests',
            data=json.dumps(
                dict(
                    rideId=rideId
                )
            ),
            content_type='application/json',
            headers=({"token": token})
        )
        

   







