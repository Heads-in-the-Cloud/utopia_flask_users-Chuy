# Flask/Python Packages
from flask import Flask, request, jsonify, make_response
from . import app
from .models.users import *                                                                 
import json
from .database import *
import jwt
import uuid


from datetime import datetime, timedelta
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash


#Decorator which checks for the token
def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = None
		# jwt is passed in the request header
		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']
		if not token:
			return jsonify({'message' : 'Token is missing !!'}), 401
		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
			current_user = User.query.filter_by(id = data['id']).first()
		except:
			return jsonify({'message' : 'Token is invalid !!'}), 401
		return f(current_user, *args, **kwargs)
	return decorated


@app.route('/user', methods =['GET'])
@token_required
def get_all_users(current_user):
	users = User.query.all()
	output = []
	for user in users:
		output.append({
			'id': user.id,
			'name' : user.given_name + user.family_name,
			'email' : user.email,
            'password': user.password
		})
	return jsonify({'users': output})


@app.route('/login', methods =['POST'])
def login():
	auth = request.form 
	if not auth or not auth.get('email') or not auth.get('password'):
		return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm ="Login required !!"'})

	user = User.query.filter_by(email = auth.get('email')).first()

	if not user:
		return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'})

	if check_password_hash(user.password, auth.get('password')):
		token = jwt.encode({
			'id': user.id,
			'exp' : datetime.utcnow() + timedelta(minutes = 30)
		}, app.config['SECRET_KEY'])
		return make_response(jsonify({'token' : token.decode('UTF-8')}), 201)
	return make_response('Could not verify', 403, {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'})


@app.route('/signup', methods =['POST'])
def signup():
	data = request.form
 
	# Get the data individually from the request
	role_id, given_name, family_name, username, password, email, phone \
 	= \
 	data.get('role_id'), \
  	data.get('given_name'),\
    data.get('family_name'),\
    data.get('username'), \
    data.get('password'), \
    data.get('email'), \
    data.get('phone')

	# checking for existing user
	user = User.query.filter_by(email = email).first()
 
	if not user:
		user = User(
			role_id 	= role_id,
            given_name 	= given_name,
            family_name = family_name,
            username	= username,
			email 		= email,
            phone 		= phone,
			password 	= generate_password_hash(password)
		)
		# insert user
		db.session.add(user)
		db.session.commit()

		return make_response('Successfully registered.', 201)
	else:
		# returns 202 if user already exists
		return make_response('User already exists. Please Log in.', 202)


    






