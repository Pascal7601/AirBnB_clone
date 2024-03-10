#!/usr/bin/python3
"""
Module: file_storage

This module defines the FileStorage class, which provides functionality to serialize instances to a JSON file and deserialize JSON file to instances.
"""

import json
from models.base_model import BaseModel

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
        """
        Serializes objects to the JSON file.

        Note:
            This method serializes all objects stored in __objects dictionary to the JSON file specified by __file_path attribute.
        """
        all_obj = self.__objects
        serial_obj = {}
        for key, obj in all_obj.items():
            serial_obj[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serial_obj, file)

    
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