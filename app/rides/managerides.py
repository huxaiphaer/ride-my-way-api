from flask import Flask,jsonify,make_response
from flask_restful import Resource, Api, reqparse
from app.model.user import User,generate_token,decode_token
import re
import json
from app.user.authentication import my_users_list
from app.model.addride import AddRide


rides_list = []



class GetRides(Resource):
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('offer_name', type=str, required=True)
        parser.add_argument('offer_details', type=str, required=True)
        parser.add_argument('offer_price', type=float, required=True)
        parser.add_argument('token', location='headers')
        
        args = parser.parse_args()
         #check the token value if its available 
        if not args['token']:
            return make_response(jsonify({"message": "Token is missing"}), 401)
        decoded = decode_token(args['token'])
        if decoded["status"] == "Failure":
            return make_response(jsonify({"message": decoded["message"]}), 401)


        for user in my_users_list:

            if user['id'] == decoded['id']:
                if decoded['isDriver'] == "True":
                    on = args['offer_name']
                    od = args['offer_details']
                    price = args['offer_price']
                    global id
                    if len(rides_list)==0:
                        id = len(rides_list)+1
                    else:
                        id = id+1
                    new_request = AddRide(id,on,od,price)
                    for ridereq in rides_list:
                        if on == ridereq['offer_name']:
                            return make_response(jsonify({"message": 'This ride offer  already exists.'}), 400)
                  
            
                    ridereq = json.loads(new_request.json())
                    rides_list.append(ridereq)
              
                    return make_response(jsonify({
                    'message': 'Ride offer created successfully.',
                    'status': 'success'},
                ), 201)
                return make_response(jsonify({"message": "Passenger  is not authorized to create meals"}), 401)

        return make_response(jsonify({"message": "Please first create an account."}), 401)

    def get(self):


        """
        Returns all ride offers  made for authenticated drivers and passengers
        token is required to get them.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('token', location='headers')
        args = parser.parse_args()
        if not args['token']:
            return make_response(jsonify({"message": "Token is missing"}), 401)
        decoded = decode_token(args['token'])
        if decoded["status"] == "Failure":
            return make_response(jsonify({"message": decoded["message"]}), 401)
       
        my_rides = []
        for ride in rides_list:
            rides_data = {
                    "id":ride["id"],
                    "offer_name": ride["offer_name"],
                    "offer_details": ride['offer_details'],
                     "offer_price": ride['offer_price']
                }
            my_rides.append(rides_data)
        if my_rides:
            return make_response(jsonify({"ride_offers": my_rides,
                                    "status": "success"}), 200)
        else:
            return make_response(jsonify({"message": "No ride offers found."}), 404)

        return make_response(jsonify({"message": "Please first create an account."}), 404)


class GetSingleRide(Resource):
    def get(self,ride_id):
        parser = reqparse.RequestParser()
        parser.add_argument('token', location='headers')      
        args = parser.parse_args()

        if not args['token']:
            return make_response(jsonify({"message": "Token is missing"}), 401)
        decoded = decode_token(args['token'])
        if decoded["status"] == "Failure":
            return make_response(jsonify({"message": decoded["message"]}), 401)
        for ride in rides_list:
            if int(ride['id']) == int(ride_id):

                rides_data = {
                    "id":ride["id"],
                    "offer_name": ride["offer_name"],
                    "offer_details": ride['offer_details'],
                     "offer_price": ride['offer_price']
                }
                
                return make_response(jsonify({"ride_offer": rides_data,
                                    "status": "success"}), 200)
        return make_response(jsonify({"message": "sorry please , ride offer not found"}), 404)
        