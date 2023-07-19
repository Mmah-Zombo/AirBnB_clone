#!/usr/bin/python3
"""Contains the entry point of the command interpreter."""

import cmd
import shlex
from models.base_model import BaseModel
from models.user import User  # Import User class
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter on EOF (Ctrl+D)."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def help_quit(self):
        """Display help message for the quit command."""
        print("Quit command to exit the command interpreter.")

    def help_EOF(self):
        """Display help message for the EOF (Ctrl+D) command."""
        print("Exit the command interpreter on EOF (Ctrl+D).")

    def help_help(self):
        """Display help message for the help command."""
        print("Show help message for the specified command \
              or list available commands.")

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print its id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        else:
            new_obj = BaseModel() if args[0] == "BaseModel" else User()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        """Show the string representation of an instance based \
            on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and \
            id (save the change into the JSON file)."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances \
            based or not on the class name."""
        objects = storage.all()
        args = shlex.split(arg)
        if not args or args[0] in ["BaseModel", "User"]:
            print([str(obj) for obj in objects.values()])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id \
            by adding or updating attribute."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key in objects:
                obj = objects[key]
                attr_name = args[2]
                attr_value = args[3]
                setattr(obj, attr_name, attr_value)
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
