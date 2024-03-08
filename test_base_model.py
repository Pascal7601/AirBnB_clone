#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
