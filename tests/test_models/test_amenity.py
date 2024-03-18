#!/usr/bin/python3
"""
Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenityInstantiation
    TestAmenitySave
    TestAmenityToDict
"""
import os
import model
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenityInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        """Test instantiation of Amenity class with no arguments."""
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        """Test if a new instance of Amenity is stored in objects."""
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test if id attribute of Amenity is a public string."""
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        """Test if created_at attribute of Amenity is a public datetime."""
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test if updated_at attribute of Amenity is a public datetime."""
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        """Test if name attribute of Amenity is a public class attribute."""
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_two_amenities_unique_ids(self):
        """Test if two instances of Amenity have unique ids."""
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_two_amenities_different_created_at(self):
        """Test if two instances of Amenity have different created_at times."""
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_two_amenities_different_updated_at(self):
        """Test if two instances of Amenity have different updated_at times."""
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_str_representation(self):
        """Test if __str__ method of Amenity provides correct string representation."""
        dt = datetime.today()
        dt_repr = repr(dt)
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        amstr = am.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

    def test_args_unused(self):
        """Test if passing None as argument to Amenity instance does not affect __dict__."""
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation of Amenity class with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        am = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(am.id, "345")
        self.assertEqual(am.created_at, dt)
        self.assertEqual(am.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation of Amenity class with None keyword arguments."""
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenitySave(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

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
        """Test saving one instance of Amenity."""
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)

    def test_two_saves(self):
        """Test saving two instances of Amenity."""
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        second_updated_at = am.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        am.save()
        self.assertLess(second_updated_at, am.updated_at)

    def test_save_with_arg(self):
        """Test saving instance of Amenity with argument."""
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

    def test_save_updates_file(self):
        """Test if save method updates the file correctly."""
        am = Amenity()
        am.save()
        amid = "Amenity." + am.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenityToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        """Test if to_dict method returns a dictionary."""
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test if to_dict method returns a dictionary with correct keys."""
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if to_dict method returns a dictionary with added attributes."""
        am = Amenity()
        am.middle_name = "Holberton"
        am.my_number = 98
        self.assertEqual("Holberton", am.middle_name)
        self.assertIn("my_number", am.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if datetime attributes in to_dict method are converted to strings."""
        am = Amenity()
        am_dict = am.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of to_dict method of Amenity."""
        dt = datetime.today()
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(am.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test that to_dict method of Amenity returns a different dictionary from the __dict__ attribute."""
        am = Amenity()
        self.assertNotEqual(am.to_dict(), am.__dict__)

    def test_to_dict_with_arg(self):
        """Test that passing an argument to to_dict method of Amenity raises a TypeError."""
        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)


if __name__ == "__main__":
    unittest.main()
