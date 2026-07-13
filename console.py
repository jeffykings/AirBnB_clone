#!/usr/bin/python3

"""contains the entry point of the command interpreter"""

import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""

    classes = {"BaseModel": BaseModel,
               "User": User,
               "Place": Place,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Review": Review
               }
    prompt = "(hbnb) "

    def precmd(self, line):
        if "." in line:
            pattern = r'^(\w+)\.(\w+)\((.*?)\)$'
            match = re.match(pattern, line)

            if match:
                class_name = match.group(1)
                command = match.group(2)
                args = match.group(3)

                # Handle update with arguments
                if command == "update":
                    import shlex

                    compa = r'^\s*("[^"]+"|\'[^\']+\')\s*,\s*(\{.*\})\s*$'
                    dict_match = re.match(compa, args, re.DOTALL)

                    if dict_match:
                        obj_id_raw, dict_raw = dict_match.groups()
                        obj_id = shlex.split(obj_id_raw)[0]

                        # Pass the dict as-is; let do_update handle it
                        return f'update {class_name} {obj_id} {dict_raw}'

                    tokens = [t.rstrip(',') for t in shlex.split(args)]
                    if len(tokens) >= 3:
                        obj_id = tokens[0]
                        attr_name = tokens[1]
                        attr_value = ' '.join(tokens[2:])

                        if re.search(r'\s|["\']', attr_value):
                            attr_value = '"' + attr_value.replace('"', r'\"') + '"'
                        return f"update {class_name} {obj_id} {attr_name} {attr_value}"
                    else:
                        return f"update {class_name} {args}"

                # Normal handling for other commands
                if args:
                    args = args.strip()
                    return f"{command} {class_name} {args}"
                else:
                    return f"{command} {class_name}"
        return line

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
        import shlex
        from models import storage
        stored_obj = storage.all()

        arg = shlex.split(line)

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

        import shlex
        from models import storage
        stored_obj = storage.all()

        arg = shlex.split(line)

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

        import shlex, ast
        from models import storage
        stored_obj = storage.all()

        arg = shlex.split(line)

        if not HBNBCommand.class_checker(arg, True):
            return

        key = f"{arg[0]}.{arg[1]}"

        if HBNBCommand.instance_checker(key) is False:
            return

        if len(arg) >= 3 and arg[2].startswith("{") and arg[2].endswith("}"):
            dict_str = ' '.join(arg[2:])
            try:
                updates = ast.literal_eval(dict_str)
            except (ValueError, SyntaxError):
                print("** invalid dictionary **")
                return

            if not isinstance(updates, dict):
                print("** invalid dictionary **")
                return

            obj = stored_obj[key]   
            for k, v in updates.items():
                setattr(obj, k, v)
            storage.save()
            return

        if not HBNBCommand.attribute_checker(arg):
            return

        obj = stored_obj[key]

        # Try to cast numbers/bools if value looks like it
        val = arg[3]
        try:
            val = ast.literal_eval(val)
        except Exception:
            pass
        setattr(obj, arg[2], val)
        storage.save()

    def do_count(self, line):
        """retrieve the number of instances of a class
        usage:
            <class name>.count().
        """

        from models import storage
        stored_obj = storage.all()

        arg = line.split()
        checker = HBNBCommand.class_checker(arg, False)
        if checker is False:
            return
        temp_list = [str(value) for key, value in stored_obj.items()
                     if key.startswith(f"{arg[0]}.")]

        print(len(temp_list))

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
            print("** attribute name missing **")
            return False

        elif len(line) < 4:
            print("** value missing **")
            return False

        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
