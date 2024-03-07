#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """initializing attributes of BaseModel class"""
        self.id = uuid.uuid4().hex
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        """returns a string of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


    def save(self):
        """updates the instance updated_at"""
        self.updated_at = datetime.now()


    def to_dict(self):
        """returns a dictionary containig key value of instance in __dict__"""
        obj_dict = self.__dict__.copy
        obj_dict['__class__'] = self.__class__.__name__

        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict


User_id = BaseModel()
print(User_id)
