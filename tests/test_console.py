#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):

    def test_help_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIn("Documented commands (type help <topic>):", f.getvalue())

    def test_help_create_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertIn("Create a new instance of BaseModel", f.getvalue())

    def test_help_show_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertIn("Prints the string representation of an instance", f.getvalue())

    def test_help_destroy_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertIn("Deletes an instance based on the class name and id", f.getvalue())

    def test_help_update_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertIn("Updates an instance based on the class name and id", f.getvalue())

    def test_create_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertIn("** class name missing **", f.getvalue())

    def test_show_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertIn("** class name missing **", f.getvalue())

    def test_destroy_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertIn("** class name missing **", f.getvalue())

    def test_update_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertIn("** class name missing **", f.getvalue())

    # Add more test cases for other commands like all, count, etc.

if __name__ == '__main__':
    unittest.main()
