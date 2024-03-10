#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """class that inherits for the BaseModel
      Attr:
      place_id - empty string
      user_id - empty string
      text - empty string"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ''
        self.user_id = ''
        self.text = ''