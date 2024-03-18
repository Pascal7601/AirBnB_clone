#!/usr/bin/python3
"""
Module: base_model

This module defines the BaseModel class, which serves as the base class for other models in the application.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class provides common functionality for other model classes.

    Attributes:
        id (str): A unique identifier generated using UUID.
        created_at (datetime): The datetime when the instance was created.
        updated_at (datetime): The datetime when the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
<<<<<<< HEAD
        """initializing attributes of BaseModel class"""
<<<<<<< HEAD
=======
        self.__dict__ = kwargs
        fileStorage.new(self)
>>>>>>> 881d6dda88403c4d39b8438c7f8b784c49529a53
=======
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Note:
            If kwargs is provided, the instance attributes are initialized using the values from kwargs.
            Otherwise, a new instance is created with unique id, created_at, and updated_at attributes.
        """

>>>>>>> e3465bf68161a007e71283296fb24ca9e9fd9017
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
        """
        Updates the updated_at attribute with the current datetime and saves the instance to the storage.

        Note:
            After calling save(), the instance's data will be persisted.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: A dictionary containing the key-value pairs of the instance attributes.

        Note:
            The returned dictionary includes the '__class__', 'created_at', and 'updated_at' keys.
        """
        obj_dicts = self.__dict__.copy()

        obj_dicts['__class__'] = self.__class__.__name__

        obj_dicts['created_at'] = self.created_at.isoformat()
        obj_dicts['updated_at'] = self.updated_at.isoformat()

        return obj_dicts

<<<<<<< HEAD
        return obj_dict
<<<<<<< HEAD
=======

>>>>>>> 881d6dda88403c4d39b8438c7f8b784c49529a53
=======
    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: A string containing the class name, id, and instance attributes.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
>>>>>>> e3465bf68161a007e71283296fb24ca9e9fd9017
