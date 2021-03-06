# ride-my-way-api
[![Build Status](https://travis-ci.org/huxaiphaer/ride-my-way-api.svg?branch=develop)](https://travis-ci.org/huxaiphaer/ride-my-way-api)
[![Coverage Status](https://coveralls.io/repos/github/huxaiphaer/ride-my-way-api/badge.svg?branch=develop)](https://coveralls.io/github/huxaiphaer/ride-my-way-api?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/4d915a0d96fd3f9c9f8a/maintainability)](https://codeclimate.com/github/huxaiphaer/ride-my-way-api/maintainability)


Ride-my App is a carpooling application
that provides drivers with the ability to create ride offers and passengers  to join available ride offers.

To acces this API online visit [API Link ](https://ride-my-way-huzaifah.herokuapp.com/)

### Requirements Building blocks.
- ```Python3``` - A programming language that lets us work more quickly (The universe loves speed!).

- ```Flask``` - A microframework for Python based on Werkzeug, Jinja 2 and good intentions.

- ```Virtualenv``` - A tool to create isolated virtual environment

### Installation on WIndows

First clone this repository
```
 git clone @https://github.com/huxaiphaer/ride-my-way-api
 cd ride-my-way-api
 ```

Create virtual environment and install it on Windows

 ```
 virtualenv --python=python3 venv
 .\venv\bin\activate.bat
 ```

Then install all the necessary dependencies by
 ```
pip install -r requirements.txt
 ```

Then run the application
 ```
 python run.py
 ```
 Testing and knowing coverage run 
 ```
nosetests or python manage.py test
 ```
