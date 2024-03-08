#!/usr/bin/python3
import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage

fileStorage = FileStorage

class BaseModel:
    def __init__(self, *args, **kwargs):
        """initializing attributes of BaseModel class"""
        self.__dict__ = kwargs
        fileStorage.new(self)
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
                if "id" not in kwargs:
                    self.id = uuid.uuid4().hex
                if "created_at" not in kwargs:
                    self.created_at = datetime.now()
                if "updated_at" not in kwargs:
                    self.updated_at = datetime.now

        else:
            self.id = uuid.uuid4().hex
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def __str__(self):
        """returns a string of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


    def save(self):
        """updates the instance updated_at"""
        #self.updated_at = datetime.now()
        fileStorage.save()


    def to_dict(self):
        """returns a dictionary containig key value of instance in __dict__"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict

