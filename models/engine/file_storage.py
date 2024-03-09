#!/usr/bin/python3
import json


class FileStorage:
    """serializes instances to JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """returns the dictionary __objects"""
        return self.__objects


    def new(self, obj):
        """sets objects """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj


    def save(self):
        """serializes objects to JSON file"""
        all_obj = self.__objects
        serial_obj = {}
        for key, obj in all_obj.items():
            serial_obj[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serial_obj, file)

    
    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                 load_obj = json.load(file)
                 for key, value in load_obj.items():
                    class_name = value['__class__']
                    obj = globals()[class_name](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
