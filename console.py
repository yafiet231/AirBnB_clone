#!/usr/bin/python3

"""
A program that contains the entry point of the command interpreter:
Which ables to manage the objects of our HBnB project.
"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):

    """
    Define commmand interpreter for HBNB application.
    """

    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Place", "State", "City",
               "Amenity", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print()
        return True

    # Make alias for quit command
    do_exit = do_quit

    def emptyline(self):
        """Nothing do, just pass upon receiving an empty line."""
        pass

    def default(self, line):
        """Default behavior if input command prefix is invalid"""
        if '.' in line:
            args = line.split('.')
            class_name = args[0]
            command_w_args = args[1]

            command, arg_w_end_bracket = command_w_args.split('(')

            # Check if the class name exists
            if class_name in self.classes:

                if len(arg_w_end_bracket) > 1:
                    # Remove the closing parenthesis
                    arg_w_quotes = arg_w_end_bracket.strip(')')
                    order = r"\{[^{}]*\}"
                    searched = re.findall(order, arg_w_quotes)
                    if searched and command == "update":
                        id_dict = arg_w_quotes.split(',', 1)[0].strip('"')
                        attr_dict = eval(searched[0])
                        self.dict_update(class_name, id_dict, attr_dict)
                        return
                    if ' ' in arg_w_quotes:
                        update_listt = arg_w_quotes.split(', ')
                        update_args = []
                        for it in update_listt:
                            split_it = it.strip().strip('"').split('"')
                            update_args.extend(split_it)

                        if command == "update":
                            update_str = ' '.join([class_name] + update_args)
                            self.do_update(update_str)
                            return

                    if '"' in arg_w_quotes and '"' in arg_w_quotes[::-1]:
                        argu = arg_w_quotes[1:-1]

                    # assign id
                    id_arg = argu
                    arg = f"{class_name} {id_arg}"

                    if command == "destroy":
                        self.do_destroy(arg)
                        return

                    elif command == "show":
                        self.do_show(arg)
                        return
                else:
                    if command == "create":
                        self.do_create(class_name)
                        return
                    elif command == "all":
                        self.do_all(class_name)
                    elif command == "count":
                        self.do_count(class_name)
            elif not class_name:
                print("** class name missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("Unknown command:", line)

    def do_create(self, name):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        if not name:
            print("** class name missing **")
            return
        elif name not in self.classes:
            print("** class doesn't exist **")
            return

        instance = eval(name)()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        objs_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in objs_dict:
            print("** no instance found **")
            return

        print(objs_dict[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        objs_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])

        if key not in objs_dict:
            print("** no instance found **")
            return

        del objs_dict[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        """

        args = arg.split()
        objs_dict = storage.all()

        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        instances = [str(objs_dict[obj]) for obj in objs_dict
                     if not args or obj.startswith(args[0] + ".")]
        print(instances)

    def do_update(self, arg):
        """Updates an instance based on the
        class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return

        objs_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in objs_dict:
            print("** no instance found **")
            return

        obj = objs_dict[key]
        setattr(obj, args[2], args[3])
        obj.save()

    def do_count(self, arg):
        """ Retrieve the number of instances of a class"""
        args = arg.split(' ')
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            searched = [
                key for key in storage.all() if key.startswith(
                    args[0] + '.')]
            print(len(searched))

    def dict_update(self, class_name, id_dict, attr_dict):
        objs_dict = storage.all()
        key = "{}.{}".format(class_name, id_dict)
        if key not in objs_dict:
            print("** no instance found **")
            return
        obj = objs_dict[key]
        for attr, value in attr_dict.items():
            setattr(obj, attr, value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
