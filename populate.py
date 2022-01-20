import random
import math
import requests
import json
from faker      import Faker
from datetime   import timedelta
from datetime   import datetime
from src.models    import *       
from werkzeug.security import generate_password_hash, check_password_hash                                                                                


fake = Faker()
PORT = 5002
apiRoute = f'http://localhost:{PORT}/signup'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


def populateUsers():
        
    for i in range(100):
        users = []
        users.append({
            "role_id": fake.pyint(min_value=1, max_value=3, step=1),
            "given_name": fake.first_name(),
            "family_name": fake.last_name(),
            "username": fake.user_name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "password": fake.password()
        })
        for i in range(len(users)):
            r = requests.post(apiRoute, data=json.dumps(users[i]), headers=headers)
            print(r.status_code)

populateUsers()

    



