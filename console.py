#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """the console object"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Called when an empty line is entered. Does nothing."""
        pass

    def do_quit(self, arg):
        """Exit the program.
        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D).
        """
        print()
        return True

    def do_help(self, arg):
        """List available commands with "help" or detailed help with "help cmd".
        Usage: help [cmd]
        """
        cmd.Cmd.do_help(self, arg)

    # Define additional commands here (e.g., create, show, update, destroy)

if __name__ == "__main__":
    # Initialize FileStorage
    storage.reload()

    # Start the command interpreter
    HBNBCommand().cmdloop()
