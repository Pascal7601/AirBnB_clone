#!/usr/bin/python3
import cmd  # Importing the cmd module for command-line interface functionality
import shlex  # Importing the shlex module for splitting command-line strings
import sys  # Importing the sys module for system-specific parameters and functions
from test_base_model import User, Note  # Importing User and Note classes from test_base_model module

class Command(cmd.Cmd):
    """
    Command-line interface class for interacting with User and Note objects.
    """
    prompt = "(hbnb) "  # Setting the prompt for the command line interface

    def do_greet(self, arg):
        """
        Greets the user with a given name.
        
        Arguments:
        arg (str): Name of the user to greet.
        """
        print("Hello", arg)

    def do_EOF(self, line):
        """
        Handles the end of file input.
        """
        print("")  # Print a newline for better formatting
        return True

    def do_create(self, line):
        """
        Creates a new object of type User or Note.

        Arguments:
        line (str): The string representation of the object to create. Should be in valid Python syntax.
        """
        x = eval(line)  # Evaluate the input string as Python code to create the object
        x.save()  # Save the created object
        print(x)  # Print the created object

    def do_quit(self, line):
        """
        Quits the command-line interface.
        """
        return True  # Return True to indicate quitting the command line

    def onecmd(self, line):
        """
        Handles the execution of commands on the interface.
        
        Arguments:
        line (str): The command to execute.
        """
        return cmd.Cmd.onecmd(self, line)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        shlex.split(sys.argv)  # Split command-line arguments if present
    Command().cmdloop()  # Start the command loop of the Command class
