#!/usr/bin/python3
""" Module for review test cases"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Class for the test cases of base review"""

    def __init__(self, *args, **kwargs):
        """ Initialization of attributes"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Method to test for place id"""
        new = self.value()
        self.assertNotEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Method to test for user id"""
        new = self.value()
        self.assertNotEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.text), str)
