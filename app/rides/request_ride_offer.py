from flask import Flask,jsonify,make_response
from flask_restful import Resource, Api, reqparse
from app.model.user import User,generate_token,decode_token
import re
import json
from app.user.authentication import my_users_list
from app.rides.managerides import rides_list,GetRides,GetSingleRide
from app.model.addride import AddRide

class RequestRideOffer(Resource):

    def post(self, rideId):

        parser = reqparse.RequestParser()
        parser.add_argument('token', location='headers')      
        args = parser.parse_args()

        if not args['token']:
            return make_response(jsonify({"message": "Token is missing"}), 401)
        decoded = decode_token(args['token'])
        if decoded["status"] == "Failure":
            return make_response(jsonify({"message": decoded["message"]}), 401)
        if decoded['isDriver'] == "False":
            return make_response(jsonify({"message": "Invalid for Drivers "}), 401)
        
        print(rides_list)
         
        #details = filter(lambda f: f['id'] == rideId, rides_list)
         
        if int(rideId) in [x['id'] for x in rides_list]:
            return make_response(jsonify({"message": "Request has been made successfully."}), 201)
        else :
            return make_response(jsonify({"message": "Sorry,No ride offers available for your request."}), 400)


        return make_response(jsonify({"message": "Invalid request, please insert again."}), 400)
        


