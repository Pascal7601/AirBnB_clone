#!/usr/bin/python3

import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Console interface for managing instances of various classes.
    """

    # Prompt for the console
    prompt = "(hbnb) "

    # List of valid class names
    class_names = ['BaseModel', 'User', 'City', 'Amenity', 'Place', 'Review', 'State']

    def do_EOF(self, line):
        """
        Handles the end of file input.
        """
        print()
        return True

    def do_quit(self, arg):
        """
        Quits the program.
        """
        return True

    def emptyline(self):
        """
        Handles an empty line input.
        """
        self.lastcmd = ''

    def do_create(self, arg):
        """
        Creates a new instance for the specified class.
        """
        # Split the argument into a list of tokens
        command = shlex.split(arg)
        if len(command) == 0:
            print('** class name missing **')
        elif command[0] not in self.class_names:
            print("** class doesn't exist **")
        else:
            # Dynamically create an instance of the specified class
            new_instance = eval(f"{command[0]}()")
            # Save the instance to the storage
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Shows the string representation of an instance.
        """
        command = shlex.split(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.class_names:
            print("** class name doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            # Retrieve all objects from storage
            objects = storage.all()
            # Construct the key for the specified instance
            key = "{}.{}".format(command[0], command[1])
            if key in objects:
                # Print the string representation of the instance
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes a class or an instance of a class.
        """
        command = shlex.split(arg)

        if len(command) == 0:
            print('** class name missing **')
        elif command[0] not in self.class_names:
            print("** class doesn't exit **")
        elif len(command) < 2:
            print("** instance id is missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(command[0], command[1])
            if key in objects:
                # Delete the specified instance from storage
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints the string representation of all instances or specific class.
        """
        objects = storage.all()
        command = shlex.split(arg)
        if len(command) == 0:
            # If no class name is provided, print all instances
            for key, value in objects.items():
                print(str(value))
        elif command[0] not in self.class_names:
            print("** class doesn't exist **")
        else:
            # If class name is provided, print instances of that class
            for key, value in objects.items():
                if key.split(".")[0] == command[0]:
                    print(str(value))

    def default(self, arg):
        """
        Handles commands on the command line.
        """
        arg_list = arg.split(".")
        new_class_name = arg_list[0]
        command = arg_list[1].split('(')

        new_method = command[0]
        extra_arg = command[1].split('(')[0]

        method_dict = {
            'all': self.do_all,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update,
            'count': self.do_count
        }
        if new_method in method_dict.keys():
            return method_dict[new_method]("{} {}".format(new_class_name, extra_arg))

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """
        Counts the number of instances.
        """
        objects = storage.all()

        command = shlex.split(arg)
        new_class_name = command[0]

        count = 0
        if command:
            if new_class_name in self.class_names:
                for obj in objects.values():
                    if obj.__class__.__name__ == new_class_name:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        """
        Updates an instance by adding or updating an attribute.
        """
        command = shlex.split(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance is missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(command[0], command[1])
            if key not in objects:
                print("** no instance found **")
            elif len(command) < 3:
                print("** attribute name missing **")
            elif len(command) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attr_name = command[2]
                attr_val = command[3]

                try:
                    attr_val = eval(attr_val)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_val)

                obj.save()

    def onecmd(self, line):
        """
        Handles execution on the interface.
        """
        return cmd.Cmd.onecmd(self, line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
