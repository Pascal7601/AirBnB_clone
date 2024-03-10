#!/usr/bin/python3

from models.base_model import BaseModel


class State(BaseModel):
    """class that inherits from BaseModel class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ''