#!/usr/bin/python3

from models.base_model import BaseModel
from models.state import State

class City(BaseModel):
    """"class that inherits from BaseModel
        Attr:
             state_id = empty string
             name = empty string"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ''
