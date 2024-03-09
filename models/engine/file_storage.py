#!/usr/bin/python3

import json

class FileStorage:
    """serializes instances to JSON file and deserializes JSON file to instances"""

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}


    def all(self):
        """returns the dictionary __objects"""
        return self.__objects


    def new(self, obj):
        """sets objects """
        key = f"{obj.__class__.name__}.{obj.id}"
        self.__objects[key] = obj


    def save(self):
        """serializes objects to JSON file"""
        serial_obj = {}
        for key, value in self.__objects.items():
            serial_obj[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(serial_obj, f)





