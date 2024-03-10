#!/usr/bin/python3
import cmd
import shlex
import sys
from models.base_model import BaseModel
from models import storage
class HBNBCommand(cmd.Cmd):
   """Defines the console"""
   prompt = "(hbnb) "
    
   class_names = ['BaseModel']


   def do_EOF(self, line):
      """handling the end of file"""
      print()
      return True
    
    
   def do_quit(self, line):
      """quitting the programme"""
      return True
    

   def do_create(self, arg):
      """creates new user for the specific classes"""
      command = shlex.split(arg)
      if len(command) == 0:
         print('** class name missing **')
      elif command[0] not in self.class_names:
         print("** class doesn't exist **")
      else:
         new_instance = BaseModel()
         new_instance.save()
         print(new_instance.id)


   def do_show(self, arg):
      """show the string representation of an instance"""
      command = shlex.split(arg)
      if len(command) == 0:
         print("** class name missing **")
      elif command[0] not in self.class_names:
         print("** class name doesn't exist **")
      elif len(command) < 2:
         print("** instance id missing **")
      else:
         objects = storage.all()
         key = "{}.{}".format(command[0], command[1])
         if key in objects:
            print(objects[key])
         else:
            print("** no instance found **")

   def do_destroy(self, arg):
      """"deletes a class or an instance of a class"""
      command = shlex.split(arg)

      if len(command) == 0:
         print('** class name missing **')
      elif command[0] not in self.class_names:
         print("** class  doesn't exit **")
      elif len(command) < 2:
         print("** instance id is missing **")
      else:
         objects = storage.all()
         key = "{}.{}".format(command[0], command[1])
         if key in objects:
            del objects[key]
            storage.save
         else:
            print("** no instance found **")

   def do_all(self, arg):
      """"prints the string representation of all instances or specific class"""
      objects = storage.all()
      command = shlex.split(arg)
      if len(command) == 0:
         for key, value in objects.items():
            print(str(value))
      elif command[0] not in self.class_names:
         print("** class doesn't exist")
      else:
         for key, value in objects.items():
            if key.split(".")[0] == command[0]:
               print(str(value))
   

   def do_update(self, arg):
      """"updates an instance by adding or updating an attribute"""
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
            attrr_name = command[2]
            attrr_val = command[3]

            try:
               attrr_val = eval(attrr_val)
            except Exception:
               pass
            setattr(obj, attrr_name, attrr_val)

            obj.save()

      

    
   def onecmd(self, line):
      """handles execution on the interface"""
      return cmd.Cmd.onecmd(self, line)


if __name__ == '__main__':
   HBNBCommand().cmdloop()
