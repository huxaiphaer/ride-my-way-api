import json

from base import BaseTestCase

class Tests_Requests(BaseTestCase):
    """Test for requests"""
    def test_rideoffers_submission_successfully(self):
        """Tests when the ride offers  are submitted successfully"""
        with self.client:
            self.register_user("huzaifah", "huz@gmail.com", "12345","True")
            token = self.get_token()
            response = self.add_ride("Easter offer","Get an offer of 30% of this","8000",token)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertEqual(data.get('message'), "Ride offer created successfully.")
            res = self.add_ride("Easter offer", "Get an offer of 30% of this", "8000",token)
            data1 = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 400)
            self.assertEqual(data1.get('message'), "This ride offer  already exists.")

    def test_get_all_rideoffers(self):
        """Tests when all ride offers are retrieved successfully"""
        with self.client:
            self.register_user("huzaifah", "huz@gmail.com", "12345","True")
            #get a token after sign up 
            token = self.get_token()

            res = self.add_ride("Easter offer","Get an offer of 30% of this","8000",token)
            data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 201)
            self.assertEqual(data.get('message'), "Ride offer created successfully.")

            response = self.get_rideoffers(token)
            self.assertEqual(response.status_code, 200)

    def test_get_no_rideoffers(self):
        """Tests when no requests are retrieved"""
        with self.client:
            self.register_user("huzaifah", "huz@gmail.com", "12345","True")
            token = self.get_token()
            self.add_ride(token, "", "", "")
            response = self.get_rideoffers(token)
            self.assertEqual(response.status_code, 404)

    def test_add_ride_offers_with_no_token(self):
        """Tests when the ride offer are submitted with no token"""
        with self.client:
            self.register_user("huzaifah", "huz@gmail.com", "12345","True")
            token = ""
            response = self.add_ride("Easter offer", "Get an offer of 30% of this", "4000",token)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertEqual(data.get('message'), "Token is missing")

    def test_gets_all_ride_offers_with_no_token(self):
        """Tests when the no token is provided when getting ride offers """
        with self.client:
            self.register_user("huzaifah", "huz@gmail.com", "12345","True")
            token = ""
            response = self.add_ride("Easter offer", "Get an offer of 30% of this", "4000",token)
            response = self.get_rideoffers(token)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertEqual(data.get('message'), "Token is missing")

    def test_gets_all_endpoints_with_expired_token(self):
        """Tests when the token expires when retrieving all endpoints"""
        with self.client:
            self.register_user("huzaifah", "huz@gmail.com", "12345","True")
            token = "aszdfvkTYOEOODCDBDJVHEDJxwjuHdx dh"
            self.add_ride("Easter offer", "Get an offer of 30% of this", "4000",token)
            response = self.get_rideoffers(token)
            self.assertEqual(response.status_code, 401)    
   

   


    def test_get_one_rideoffer_with_expired_token(self):
        """Tests when one ride offer is retrieved with expired token"""
        with self.client:
            self.register_user("huzaifah", "huz@gmail.com", "12345","True")
            token = "zxcvb"
            self.add_ride("Easter offer", "Get an offer of 30% of this", "4000",token)
            response = self.get_one_rideoffer(token)
            self.assertEqual(response.status_code, 401)


    # def test_ride_offer_request(self):
    #     with self.client:
    #         self.register_user("huzaifah", "huz@gmail.com", "12345","True")
    #         token = self.get_token()
    #         response = self.add_ride("Easter offer","Get an offer of 30% of this","8000",token)
    #         data = json.loads(response.data.decode())
    #         self.assertEqual(response.status_code, 201)
    #         self.assertEqual(data.get('message'), "Ride offer created successfully.")
    #         res = self.request_ride_offer("1",token)
    #         data1 = json.loads(res.data.decode())
    #         self.assertEqual(res.status_code, 201)
    #         self.assertEqual(data1.get('message'), "Request has been made successfully.")
            


   