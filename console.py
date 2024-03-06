#!/usr/bin/python3
import cmd


class Command(cmd.Cmd):
    prompt = "(hbnb) "


   def do_greet(self, arg):
       """greets the user"""
        print("Hello", arg)


   def do_EOF(self, line):
       """handling the end of file"""
        print("")
        return True


   def do_quit(self, line):
       """quitting the command line"""
        return True


   def onecmd(self, line):
       """handles execution on the interface"""
        return cmd.Cmd.onecmd(self, line)


if __name__ == '__main__':
    Command().cmdloop()
