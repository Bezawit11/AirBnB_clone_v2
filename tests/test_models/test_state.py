#!/usr/bin/python3
""" Module that implements the test cases for State"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ The class test for AirBnB states"""

    def __init__(self, *args, **kwargs):
        """ Initialize the attributes"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Method that validates and tests for name"""
        new = self.value()
        self.assertNotEqual(type(new.name), str)
