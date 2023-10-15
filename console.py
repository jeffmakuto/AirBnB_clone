#!/usr/bin/python3

"""modules for the command interpreter"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Defines the command interpreter
    Attributes:
        prompt (str): The command prompt.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Quit command to exit the program. """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program. """
        print("")
        return True

    def emptyline(self):
        """ Do nothing on empty line. """
        pass

    def do_create(self, arg):
        """ Usage: create <class>
            Create a new class instance and print its id.
        """
        args = arg.split()

        if len(args) != 2:
            print("** class name missing **")
        else:
            class_name = args[1]
            
            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                new_instance = eval(class_name)()
                print(new_instance.id)
                models.storage.save()

    def do_show(self, arg):
        """ Usage: show <class> <id> or <class>.show(<id>)
            Display the string representation of a class instance of a given id.
        """
        args = arg.split()

        if len(args) < 2:
            print("** class name and/or instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]

            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                obj_key = "{}.{}".format(class_name, instance_id)

                if obj_key not in models.storage.all():
                    print("** no instance found **")
                else:
                    print(models.storage.all()[obj_key])

    def do_destroy(self, arg):
        """ Usage: destroy <class> <id> or <class>.destroy(<id>)
            Delete a class instance of a given id.
        """
        args = arg.split()

        if len(arg_elements) < 2:
            print("** class name and/or instance id missing **")
        else:
            class_name = arg_elements[0]
            instance_id = arg_elements[1]

            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                obj_key = "{}.{}".format(class_name, instance_id)

                objdict = models.storage.all()
                if obj_key not in objdict:
                    print("** no instance found **")
                else:
                    del objdict[obj_key]
                    models.storage.save()

    def do_all(self, arg):
        """ Usage: all or all <class> or <class>.all()
            Display string representations of all instances of a given class.
            If no class is specified, displays all instantiated objects.
        """
        args = arg.split()

        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []

            for obj in models.storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    obj_list.append(str(obj))
                elif len(args) == 0:
                    obj_list.append(str(obj))

            print(obj_list)

    def do_update(self, args):
        """ Usage: update <class> <id> <attribute_name> <attribute_value> or
            <class>.update(<id>, <attribute_name>, <attribute_value>) or
            <class>.update(<id>, <dictionary>)
            Update a class instance of a given id by adding or updating
            a given attribute key/value pair or dictionary.
        """
        args_list = args.split()

        if len(args_list) < 2:
            print("** class name and/or instance id missing **")
            return False

        class_name = args_list[0]
        instance_id = args_list[1]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False

        obj_key = "{}.{}".format(class_name, instance_id)
        obj_dict = models.storage.all()

        if obj_key not in obj_dict:
            print("** no instance found **")
            return False

        if len(args_list) == 2:
            print("** attribute name missing **")
            return False

        if len(args_list) == 3:
            try:
                eval_value = eval(args_list[2])
                if not isinstance(eval_value, dict):
                    print("** value missing **")
                    return False
            except NameError:
                print("** value missing **")
                return False

        obj_instance = obj_dict[obj_key]

        if len(args_list) == 4:
            attribute_name = args_list[2]
            attribute_value = args_list[3]

            if hasattr(obj_instance, attribute_name):
                setattr(obj_instance, attribute_name, type(getattr(obj_instance, attribute_name))(attribute_value))
            else:
                setattr(obj_instance, attribute_name, attribute_value)

        elif isinstance(eval(args_list[2]), dict):
            attributes_dict = eval(args_list[2])

            for key, value in attributes_dict.items():
                setattr(obj_instance, key, type(getattr(obj_instance, key))(value))

        models.storage.save()

    def do_count(self, arg):
        """ Usage: count <class> or <class>.count()
            Retrieve the number of instances of a given class.
        """
        arg_elements = arg.split()

        if len(arg_elements) == 0:
            print("** class name missing **")
            return

        class_name = arg_elements[0]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        count = 0
        for obj in models.storage.all().values():
            if class_name == obj.__class__.__name__:
                count += 1

        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
