#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD

import json
=======
=======
"""
Module: file_storage

This module defines the FileStorage class, which provides functionality to serialize instances to a JSON file and deserialize JSON file to instances.
"""

>>>>>>> e3465bf68161a007e71283296fb24ca9e9fd9017
import json
from models.base_model import BaseModel
>>>>>>> 881d6dda88403c4d39b8438c7f8b784c49529a53

class FileStorage:
    """serializes instances to JSON file and deserializes JSON file to instances"""

    """
    FileStorage class serializes instances to a JSON file and deserializes JSON file to instances.

    Attributes:
        __file_path (str): The path to the JSON file used for serialization.
        __objects (dict): A dictionary containing serialized instances.
    """

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """
        Retrieves all serialized instances.

        Returns:
            dict: A dictionary containing all serialized instances.
        """
        return self.__objects


    def new(self, obj):
        """
        Adds a new object to the __objects dictionary.

        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj


    def save(self):
<<<<<<< HEAD
        """serializes objects to JSON file"""
<<<<<<< HEAD
        serial_obj = {}
        for key, value in self.__objects.items():
            serial_obj[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(serial_obj, f)





=======
=======
        """
        Serializes objects to the JSON file.
>>>>>>> e3465bf68161a007e71283296fb24ca9e9fd9017

        Note:
            This method serializes all objects stored in __objects dictionary to the JSON file specified by __file_path attribute.
        """
        all_obj = self.__objects
        serial_obj = {}
        for key, obj in all_obj.items():
            serial_obj[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serial_obj, file)

    
<<<<<<< HEAD
    """def reload(self):
        if self.__file_path:
            with open(self.__file_path, "r") as f:"""
>>>>>>> 881d6dda88403c4d39b8438c7f8b784c49529a53
=======
    def reload(self):
        """
        Deserializes JSON file to load objects into memory.

        Note:
            This method reads the JSON file specified by __file_path attribute and deserializes its contents to load objects into the __objects dictionary.
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                 load_obj = json.load(file)
                 for key, value in load_obj.items():
                    class_name, obj_id = key.split('.')
                    try:
                        cls = eval(class_name)
                    except NameError:
                        cls = BaseModel
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
>>>>>>> e3465bf68161a007e71283296fb24ca9e9fd9017
