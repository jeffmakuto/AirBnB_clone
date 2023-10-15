#!/usr/bin/python3

"""modules for the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """ Defines the command interpreter
    Attributes:
        prompt (str): The command prompt.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Quit command to exit the program. """
        exit()

    def do_EOF(self, arg):
        """ EOF command to exit the program. """
        print("")
        exit()

    def emptyline(self):
        """ Do nothing on empty line. """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
