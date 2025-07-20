#!/usr/bin/python3

"""contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""

    prompt = "(hbnb) "

    def emptyline(self):
        return

    def do_quit(self, line):
        """Quit command to exit the program

        """

        return True

    def do_EOF(self, line):
        """ typing Ctrl-D will drop us out of the interpreter.

        """

        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
