#!/usr/bin/python3

"""contains the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""

    classes = {"BaseModel": BaseModel,
               }
    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
and prints the id.

        """

        arg = line.split()

        if not HBNBCommand.class_checker(arg, False):
            return

        new_model = type(self).classes[arg[0]]()
        new_model.save()
        print(f"{new_model.id}")

    def do_show(self, line):
        """Prints the string representation of an instance based on the
        class name and id.
        """
        from models import storage
        stored_obj = storage.all()

        arg = line.split()

        checker = HBNBCommand.class_checker(arg, True)
        if checker is False:
            return

        key = f"{arg[0]}.{arg[1]}"

        if HBNBCommand.instance_checker(key) is False:
            return

        print(f"{stored_obj[key]}")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """

        from models import storage
        stored_obj = storage.all()

        arg = line.split()

        checker = HBNBCommand.class_checker(arg, True)
        if checker is False:
            return

        key = f"{arg[0]}.{arg[1]}"

        if HBNBCommand.instance_checker(key) is False:
            return

        del stored_obj[key]
        storage.save()

    def do_all(self, line):
        """ Prints all string representation of all instances based or
        not on the class name.

        usage:  $ all BaseModel or $ all
        """

        temp_array = []
        from models import storage
        stored_obj = storage.all()

        arg = line.split()

        if not arg:
            print([str(value) for value in stored_obj.values()])
        else:
            checker = HBNBCommand.class_checker(arg, False)
            if checker is False:
                return
            print([str(value) for key, value in stored_obj.items()
                   if key.startswith(f"{arg[0]}.")])

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding
            or updating attribute (save the change into the JSON file).

            Usage:
                update <class name> <id> <attribute name> "<attribute value>"
        """

        import shlex
        from models import storage
        stored_obj = storage.all()

        arg = shlex.split(line)

        if not HBNBCommand.class_checker(arg, True):
            return

        key = f"{arg[0]}.{arg[1]}"

        if HBNBCommand.instance_checker(key) is False:
            return

        if not HBNBCommand.attribute_checker(arg):
            return

        obj = stored_obj[key]
        setattr(obj, arg[2], arg[3])
        storage.save()

    def emptyline(self):
        pass

    def do_quit(self, line):
        """Quit command to exit the program

        """

        return True

    def do_EOF(self, line):
        """ typing Ctrl-D will drop us out of the interpreter.

        """

        return True

    @staticmethod
    def class_checker(arg, check):
        """class and id checker to know if they exist"""

        if not arg:
            print("** class name missing **")
            return False

        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False

        elif check and len(arg) < 2:
            print("** instance id missing **")
            return False
        else:
            return True

    @staticmethod
    def instance_checker(key):
        """checks if a key is valid"""

        from models import storage
        stored_obj = storage.all()

        check_instance = stored_obj.get(key, None)
        if check_instance is None:
            print("** no instance found **")
            return False
        else:
            return True

    @staticmethod
    def attribute_checker(line):
        """checks if attribute and value exists"""

        if len(line) < 3:
            print("** attribute name missing ** ")
            return False

        elif len(line) < 4:
            print("** value missing **")
            return False

        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
