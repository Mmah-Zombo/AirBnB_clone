#!/usr/bin/python3
"""Contains the entry point of the command interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter on EOF (Ctrl+D)."""
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
        print("Show help message for the specified \
              command or list available commands.")

    def help_create(self):
        """Display help message for the create command."""
        print("Create a new instance of BaseModel, save it, and print its id.")

    def help_show(self):
        """Display help message for the show command."""
        print("Show the string representation of an instance \
              based on the class name and id.")

    # Add other command help methods as needed


if __name__ == '__main__':
    HBNBCommand().cmdloop()
