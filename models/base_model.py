#!/usr/bin/python3
import uuid


class BaseModel:
    def __init__(self):
        """initializing attributes of BaseModel class"""
        self.id = uuid.uuid4().hex
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()


User_id = BaseModel()
print(User_id.id)


