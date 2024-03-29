#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """Unit tests for the console.py file."""

    def test_help_command(self):
        """Test the 'help' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIn("Documented commands (type help <topic>):", f.getvalue())

    def test_help_create_command(self):
        """Test the 'help create' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertIn("Create a new instance of BaseModel", f.getvalue())

    def test_help_show_command(self):
        """Test the 'help show' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertIn("Prints the string representation of an instance", f.getvalue())

    def test_help_all_command(self):
        """Test the 'help all' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertIn("Prints all string representation of all instances", f.getvalue())

    def test_help_destroy_command(self):
        """Test the 'help destroy' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertIn("Deletes an instance based on the class name and id", f.getvalue())

    def test_help_update_command(self):
        """Test the 'help update' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertIn("Updates an instance based on the class name and id", f.getvalue())

    def test_help_count_command(self):
        """Test the 'help count' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            self.assertIn("Retrieve the number of instances of a class", f.getvalue())

    def test_help_quit_command(self):
        """Test the 'help quit' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertIn("Exit the program", f.getvalue())

    # Add more similar test methods for other help commands

    def test_create_command(self):
        """Test the 'create' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertIn("** class name missing **", f.getvalue())

    def test_show_command(self):
        """Test the 'show' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertIn("** class name missing **", f.getvalue())

    def test_all_command(self):
        """Test the 'all' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertIn("[]", f.getvalue())

    def test_destroy_command(self):
        """Test the 'destroy' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertIn("** class name missing **", f.getvalue())

    def test_update_command(self):
        """Test the 'update' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertIn("** class name missing **", f.getvalue())

    def test_count_command(self):
        """Test the 'count' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count")
            self.assertIn("** class name missing **", f.getvalue())

    def test_quit_command(self):
        """Test the 'quit' command."""
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("quit")

if __name__ == '__main__':
    unittest.main()
