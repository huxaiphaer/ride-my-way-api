from flask import Flask,jsonify,make_response
from flask_restful import Resource, Api, reqparse
from app.model.user import User,generate_token,decode_token
import re
import json

my_users_list = []

class SignUp(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        parser.add_argument('isDriver', type=str, required=True)

        args = parser.parse_args()
        username = args['username']
        email = args['email']
        password = args['password']
        isDriver = args['isDriver']

        if username.strip() == "" or len(username.strip()) < 2:
            return make_response(jsonify({"message": 
            "invalid username, Enter correct username please"}),
             400)

        if re.compile('[!@#$%^&*:;?><.0-9]').match(username):
            return make_response(jsonify({"message": 
            "Invalid characters not allowed"}), 
            400)

        if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
            return make_response(jsonify({"message": 
            "Enter valid email"}), 
            400)

        if password.strip() == "":
            return make_response(jsonify({"message": 
            "Enter password"}), 
            400)

        if len(password) < 5:
            return make_response(jsonify({"message": 
            "Password is too short, < 5"}), 
            400)

        new_user = User(username, email, password,isDriver)

        for user in my_users_list:
            if email == user['email']:
                return make_response(jsonify({"message": 
                "email already in use"}), 
                400)

        my_users_list.append(json.loads(new_user.json()))
        return make_response(jsonify({'message': 
        'User successfully created',
         'email': new_user.email}),
          201)


class Login(Resource):
    def post(self):
        """
        Allows users to login to their accounts
        """
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)

        args = parser.parse_args()
        email = args['email']
        password = args['password']

        for user in my_users_list:
            if email == user['email'] and password == user['password']:
                access_token = "{}".format(
                    generate_token(user['id'], user['isDriver']))
                return make_response(jsonify({"token": access_token,
                                              "message": "User logged in successfully"
                                              }), 200)
            return make_response(jsonify({"message": "wrong credentials"}),
             401)