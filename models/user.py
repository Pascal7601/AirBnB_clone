#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """"a class that inherits from BaseModel
    Attr:
         email - empty string
         password - empty string
         first_name - empty string
         last_name - empty string"""
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
        