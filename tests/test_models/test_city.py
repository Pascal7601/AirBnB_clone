#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModelInstantiation
    TestBaseModelSave
    TestBaseModelToDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModelInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        """Test instantiation of BaseModel class with no arguments."""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        """Test if a new instance of BaseModel is stored in objects."""
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test if id attribute of BaseModel is a public string."""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        """Test if created_at attribute of BaseModel is a public datetime."""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test if updated_at attribute of BaseModel is a public datetime."""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        """Test if two instances of BaseModel have unique ids."""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        """Test if two instances of BaseModel have different created_at times."""
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        """Test if two instances of BaseModel have different updated_at times."""
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        """Test if __str__ method of BaseModel provides correct string representation."""
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_args_unused(self):
        """Test if passing None as argument to BaseModel instance does not affect __dict__."""
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation of BaseModel class with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation of BaseModel class with None keyword arguments."""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        """Test instantiation of BaseModel class with arguments and keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)


class TestBaseModelSave(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUpClass(cls):
        """Set up class to handle file operations."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Tear down class and clean up files."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """Test saving one instance of BaseModel."""
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        """Test saving two instances of BaseModel."""
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        """Test saving instance of BaseModel with argument."""
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        """Test if save method updates the file correctly."""
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class TestBaseModelToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        """Test if to_dict method returns a dictionary."""
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test if to_dict method returns a dictionary with correct keys."""
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("_class_", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if to_dict method returns a dictionary with added attributes."""
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if datetime attributes in to_dict method are converted to strings."""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of to_dict method of BaseModel."""
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '_class_': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test that to_dict method of BaseModel returns a different dictionary from the __dict__ attribute."""
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        """Test that passing an argument to to_dict method of BaseModel raises a TypeError."""
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


if __name__ == "__main__":
    unittest.main()
