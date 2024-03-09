#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """initializing attributes of BaseModel class"""
        
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)

                setattr(self, key, value)

        else:
            self.id = uuid.uuid4().hex
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)


    def save(self):
        """updates the instance updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()
        


    def to_dict(self):
        """returns a dictionary containig key value of instance in __dict__"""
        obj_dicts = self.__dict__.copy()


    
        obj_dicts['__class__'] = self.__class__.__name__

        obj_dicts['created_at'] = self.created_at.isoformat()
        obj_dicts['updated_at'] = self.updated_at.isoformat()

        return obj_dicts
    

    def __str__(self):
        """returns a string of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

