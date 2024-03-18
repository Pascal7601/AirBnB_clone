#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUserInstantiation
    TestUserSave
    TestUserToDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUserInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        """Test instantiation of User class with no arguments."""
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        """Test if a new instance of User is stored in objects."""
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test if id attribute of User is a public string."""
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        """Test if created_at attribute of User is a public datetime."""
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test if updated_at attribute of User is a public datetime."""
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        """Test if email attribute of User is a public string."""
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        """Test if password attribute of User is a public string."""
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        """Test if first_name attribute of User is a public string."""
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        """Test if last_name attribute of User is a public string."""
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        """Test if two instances of User have unique ids."""
        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)

    def test_two_users_different_created_at(self):
        """Test if two instances of User have different created_at times."""
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_users_different_updated_at(self):
        """Test if two instances of User have different updated_at times."""
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.updated_at, us2.updated_at)

    def test_str_representation(self):
        """Test if __str__ method of User provides correct string representation."""
        dt = datetime.today()
        dt_repr = repr(dt)
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        usstr = us.__str__()
        self.assertIn("[User] (123456)", usstr)
        self.assertIn("'id': '123456'", usstr)
        self.assertIn("'created_at': " + dt_repr, usstr)
        self.assertIn("'updated_at': " + dt_repr, usstr)

    def test_args_unused(self):
        """Test if passing None as argument to User instance does not affect __dict__."""
        us = User(None)
        self.assertNotIn(None, us.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation of User class with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        us = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(us.id, "345")
        self.assertEqual(us.created_at, dt)
        self.assertEqual(us.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation of User class with None keyword arguments."""
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUserSave(unittest.TestCase):
    """Unittests for testing save method of the User class."""

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
        """Test saving User instance."""
        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        self.assertLess(first_updated_at, us.updated_at)

    def test_two_saves(self):
        """Test saving User instance twice."""
        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        second_updated_at = us.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        us.save()
        self.assertLess(second_updated_at, us.updated_at)

    def test_save_with_arg(self):
        """Test saving User instance with argument."""
        us = User()
        with self.assertRaises(TypeError):
            us.save(None)

    def test_save_updates_file(self):
        """Test if save method updates the file correctly."""
        us = User()
        us.save()
        usid = "User." + us.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())


class TestUserToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        """Test if to_dict method returns a dictionary."""
        us = User()
        self.assertTrue(dict, type(us.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test if to_dict method returns a dictionary with correct keys."""
        us = User()
        self.assertIn("id", us.to_dict())
        self.assertIn("created_at", us.to_dict())
        self.assertIn("updated_at", us.to_dict())
        self.assertIn("__class__", us.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if to_dict method returns a dictionary with added attributes."""
        us = User()
        us.middle_name = "Holberton"
        us.my_number = 98
        self.assertEqual("Holberton", us.middle_name)
        self.assertIn("my_number", us.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if datetime attributes in to_dict method are converted to strings."""
        us = User()
        us_dict = us.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of to_dict method of User."""
        dt = datetime.today()
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(us.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test that to_dict method of User returns a different dictionary from the __dict__ attribute."""
        us = User()
        self.assertNotEqual(us.to_dict(), us.__dict__)

    def test_to_dict_with_arg(self):
        """Test that passing an argument to to_dict method of User raises a TypeError."""
        us = User()
        with self.assertRaises(TypeError):
            us.to_dict(None)


if __name__ == "__main__":
    unittest.main()
