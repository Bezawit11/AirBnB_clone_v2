#!/usr/bin/python3
""" Module test for user"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ The test cases for User"""

    def __init__(self, *args, **kwargs):
        """ Creating the instance attributes for User test"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Method that tests for first name"""
        new = self.value()
        self.assertNotEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Method that tests for last name"""
        new = self.value()
        self.assertNotEqual(type(new.last_name), str)

    def test_email(self):
        """ Method that test for email of user"""
        new = self.value()
        self.assertNotEqual(type(new.email), str)

    def test_password(self):
        """ Method that validate and tests for password"""
        new = self.value()
        self.assertNotEqual(type(new.password), str)
