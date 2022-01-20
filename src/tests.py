import unittest

from src import db
from src.models import User
# from src.tests.base import BaseTestCase


class TestUserModel():

    def test_encode_auth_token(self):
        user = User(
            email='test@test.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

if __name__ == '__main__':
    unittest.main()